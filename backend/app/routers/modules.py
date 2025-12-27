from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app import models, schemas
from app.routers.auth import get_current_user

router = APIRouter()


@router.get("/", response_model=List[schemas.ModuleSummary])
def get_all_modules(db: Session = Depends(get_db)):
    modules = db.query(models.Module).order_by(models.Module.number).all()
    result = []
    for m in modules:
        lesson_count = db.query(models.Lesson).filter(models.Lesson.module_id == m.id).count()
        result.append(schemas.ModuleSummary(
            id=m.id,
            number=m.number,
            title=m.title,
            duration_hours=m.duration_hours,
            part=m.part,
            lesson_count=lesson_count
        ))
    return result


@router.get("/user-access")
def get_user_module_access(
    session_token: Optional[str] = Cookie(None),
    db: Session = Depends(get_db)
):
    user = get_current_user(session_token, db)
    if not user:
        return {"modules": [], "authenticated": False}
    
    # Admin has access to all
    if user.is_admin:
        modules = db.query(models.Module).all()
        return {
            "modules": [{"module_id": m.id, "unlocked": True} for m in modules],
            "authenticated": True,
            "is_admin": True
        }
    
    # Get user's module access
    access_list = db.query(models.UserModuleAccess).filter(
        models.UserModuleAccess.user_id == user.id
    ).all()
    
    return {
        "modules": [{"module_id": a.module_id, "unlocked": a.unlocked} for a in access_list],
        "authenticated": True,
        "is_admin": False
    }


@router.get("/part/{part_number}", response_model=List[schemas.ModuleSummary])
def get_modules_by_part(part_number: int, db: Session = Depends(get_db)):
    modules = db.query(models.Module).filter(models.Module.part == part_number).order_by(models.Module.number).all()
    result = []
    for m in modules:
        lesson_count = db.query(models.Lesson).filter(models.Lesson.module_id == m.id).count()
        result.append(schemas.ModuleSummary(
            id=m.id,
            number=m.number,
            title=m.title,
            duration_hours=m.duration_hours,
            part=m.part,
            lesson_count=lesson_count
        ))
    return result


@router.get("/{module_id}", response_model=schemas.Module)
def get_module(module_id: int, db: Session = Depends(get_db)):
    module = db.query(models.Module).filter(models.Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Modul nije pronađen")
    return module


@router.get("/number/{module_number}", response_model=schemas.Module)
def get_module_by_number(module_number: int, db: Session = Depends(get_db)):
    module = db.query(models.Module).filter(models.Module.number == module_number).first()
    if not module:
        raise HTTPException(status_code=404, detail="Modul nije pronađen")
    return module
