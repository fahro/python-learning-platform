from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
import secrets

from app.database import get_db
from app.models import User, UserModuleAccess, Module
from app.schemas import UserRegister, UserLogin, UserResponse

router = APIRouter()

# Simple session store (in production use Redis)
sessions = {}


def get_current_user(session_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    if not session_token or session_token not in sessions:
        return None
    user_id = sessions[session_token]
    return db.query(User).filter(User.id == user_id).first()


def require_user(session_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    user = get_current_user(session_token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Morate biti prijavljeni")
    return user


def require_admin(session_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    user = require_user(session_token, db)
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Samo admin može pristupiti")
    return user


@router.post("/register", response_model=UserResponse)
def register(data: UserRegister, response: Response, db: Session = Depends(get_db)):
    # Check if username exists
    existing = db.query(User).filter(User.username == data.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Korisničko ime već postoji")
    
    # Create user
    user = User(username=data.username)
    user.set_password(data.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    # Unlock first module automatically
    first_module = db.query(Module).filter(Module.number == 1).first()
    if first_module:
        access = UserModuleAccess(
            user_id=user.id,
            module_id=first_module.id,
            unlocked=True,
            unlocked_at=datetime.utcnow()
        )
        db.add(access)
        db.commit()
    
    # Create session
    token = secrets.token_hex(32)
    sessions[token] = user.id
    response.set_cookie(key="session_token", value=token, httponly=True, samesite="lax")
    
    return user


@router.post("/login", response_model=UserResponse)
def login(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not user.check_password(data.password):
        raise HTTPException(status_code=401, detail="Pogrešno korisničko ime ili lozinka")
    
    # Create session
    token = secrets.token_hex(32)
    sessions[token] = user.id
    response.set_cookie(key="session_token", value=token, httponly=True, samesite="lax")
    
    return user


@router.post("/logout")
def logout(response: Response, session_token: Optional[str] = Cookie(None)):
    if session_token and session_token in sessions:
        del sessions[session_token]
    response.delete_cookie("session_token")
    return {"message": "Uspješno ste se odjavili"}


@router.get("/me", response_model=UserResponse)
def get_me(user: User = Depends(require_user)):
    return user


@router.get("/check")
def check_auth(user: Optional[User] = Depends(get_current_user)):
    if user:
        return {"authenticated": True, "user": {"id": user.id, "username": user.username, "is_admin": user.is_admin}}
    return {"authenticated": False, "user": None}
