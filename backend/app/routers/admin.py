from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import datetime

from app.database import get_db
from app.models import User, UserModuleAccess, Module, ExerciseSubmission, QuizAttempt, Lesson
from app.schemas import UserResponse, ModuleAccessUpdate, AdminUserStats
from app.routers.auth import require_admin

router = APIRouter()


@router.get("/users", response_model=List[UserResponse])
def get_all_users(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_admin == False).all()
    return users


@router.get("/users/{user_id}/stats")
def get_user_stats(user_id: int, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen")
    
    # Get unlocked modules
    unlocked = db.query(UserModuleAccess).filter(
        UserModuleAccess.user_id == user_id,
        UserModuleAccess.unlocked == True
    ).all()
    
    # Get completed exercises
    exercises_passed = db.query(ExerciseSubmission).filter(
        ExerciseSubmission.user_id == user_id,
        ExerciseSubmission.passed == True
    ).count()
    
    # Get passed quizzes
    quizzes_passed = db.query(QuizAttempt).filter(
        QuizAttempt.user_id == user_id,
        QuizAttempt.passed == True
    ).count()
    
    # Get last activity
    last_exercise = db.query(func.max(ExerciseSubmission.submitted_at)).filter(
        ExerciseSubmission.user_id == user_id
    ).scalar()
    last_quiz = db.query(func.max(QuizAttempt.attempted_at)).filter(
        QuizAttempt.user_id == user_id
    ).scalar()
    last_activity = max(filter(None, [last_exercise, last_quiz]), default=None)
    
    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "is_admin": user.is_admin,
            "created_at": user.created_at
        },
        "modules_unlocked": [a.module_id for a in unlocked],
        "exercises_passed": exercises_passed,
        "quizzes_passed": quizzes_passed,
        "last_activity": last_activity
    }


@router.get("/users/{user_id}/progress")
def get_user_progress(user_id: int, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen")
    
    modules = db.query(Module).order_by(Module.number).all()
    result = []
    
    for module in modules:
        # Check if unlocked
        access = db.query(UserModuleAccess).filter(
            UserModuleAccess.user_id == user_id,
            UserModuleAccess.module_id == module.id
        ).first()
        
        lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
        lesson_progress = []
        
        for lesson in lessons:
            # Get exercise status
            exercise_passed = db.query(ExerciseSubmission).filter(
                ExerciseSubmission.user_id == user_id,
                ExerciseSubmission.lesson_id == lesson.id,
                ExerciseSubmission.passed == True
            ).first() is not None
            
            # Get quiz status
            quiz_attempt = db.query(QuizAttempt).filter(
                QuizAttempt.user_id == user_id,
                QuizAttempt.lesson_id == lesson.id
            ).order_by(QuizAttempt.attempted_at.desc()).first()
            
            lesson_progress.append({
                "lesson_id": lesson.id,
                "title": lesson.title,
                "exercise_passed": exercise_passed,
                "quiz_passed": quiz_attempt.passed if quiz_attempt else False,
                "quiz_score": quiz_attempt.score if quiz_attempt else None
            })
        
        result.append({
            "module_id": module.id,
            "module_number": module.number,
            "title": module.title,
            "unlocked": access.unlocked if access else False,
            "lessons": lesson_progress
        })
    
    return result


@router.post("/unlock-module")
def unlock_module(data: ModuleAccessUpdate, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen")
    
    module = db.query(Module).filter(Module.id == data.module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Modul nije pronađen")
    
    # Check if access record exists
    access = db.query(UserModuleAccess).filter(
        UserModuleAccess.user_id == data.user_id,
        UserModuleAccess.module_id == data.module_id
    ).first()
    
    if access:
        access.unlocked = data.unlocked
        access.unlocked_at = datetime.utcnow() if data.unlocked else None
        access.unlocked_by = admin.id if data.unlocked else None
    else:
        access = UserModuleAccess(
            user_id=data.user_id,
            module_id=data.module_id,
            unlocked=data.unlocked,
            unlocked_at=datetime.utcnow() if data.unlocked else None,
            unlocked_by=admin.id if data.unlocked else None
        )
        db.add(access)
    
    db.commit()
    
    return {"message": f"Modul {'otkljucan' if data.unlocked else 'zaključan'} za korisnika {user.username}"}


@router.get("/modules")
def get_all_modules(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    modules = db.query(Module).order_by(Module.number).all()
    return [{"id": m.id, "number": m.number, "title": m.title} for m in modules]


@router.delete("/users/{user_id}")
def delete_user(user_id: int, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen")
    if user.is_admin:
        raise HTTPException(status_code=400, detail="Ne možete obrisati admina")
    
    # Delete related records
    db.query(UserModuleAccess).filter(UserModuleAccess.user_id == user_id).delete()
    db.query(ExerciseSubmission).filter(ExerciseSubmission.user_id == user_id).delete()
    db.query(QuizAttempt).filter(QuizAttempt.user_id == user_id).delete()
    db.delete(user)
    db.commit()
    
    return {"message": "Korisnik obrisan"}
