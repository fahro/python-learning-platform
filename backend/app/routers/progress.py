from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app import models, schemas

router = APIRouter()


@router.get("/user/{user_id}", response_model=List[schemas.UserProgressResponse])
def get_user_progress(user_id: str, db: Session = Depends(get_db)):
    progress = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == user_id
    ).all()
    return progress


@router.get("/user/{user_id}/stats", response_model=schemas.UserStats)
def get_user_stats(user_id: str, db: Session = Depends(get_db)):
    total_lessons = db.query(models.Lesson).count()
    completed = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == user_id,
        models.UserProgress.completed == True
    ).count()
    
    total_hours = db.query(models.Module).with_entities(
        models.Module.duration_hours
    ).all()
    total_hours = sum(h[0] for h in total_hours)
    
    # Calculate completed hours
    completed_lessons = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == user_id,
        models.UserProgress.completed == True
    ).all()
    
    completed_hours = 0
    for p in completed_lessons:
        lesson = db.query(models.Lesson).filter(models.Lesson.id == p.lesson_id).first()
        if lesson:
            completed_hours += lesson.duration_hours
    
    progress_percentage = (completed / total_lessons * 100) if total_lessons > 0 else 0
    
    return schemas.UserStats(
        total_lessons=total_lessons,
        completed_lessons=completed,
        progress_percentage=round(progress_percentage, 1),
        total_hours=total_hours,
        completed_hours=completed_hours
    )


@router.post("/update")
def update_progress(progress: schemas.ProgressUpdate, db: Session = Depends(get_db)):
    existing = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == progress.user_id,
        models.UserProgress.lesson_id == progress.lesson_id
    ).first()
    
    if existing:
        existing.completed = progress.completed
        existing.code_submission = progress.code_submission
        if progress.completed:
            existing.completed_at = datetime.utcnow()
    else:
        new_progress = models.UserProgress(
            user_id=progress.user_id,
            lesson_id=progress.lesson_id,
            completed=progress.completed,
            code_submission=progress.code_submission,
            completed_at=datetime.utcnow() if progress.completed else None
        )
        db.add(new_progress)
    
    db.commit()
    return {"message": "Napredak ažuriran"}


@router.get("/user/{user_id}/module/{module_id}")
def get_module_progress(user_id: str, module_id: int, db: Session = Depends(get_db)):
    lessons = db.query(models.Lesson).filter(models.Lesson.module_id == module_id).all()
    lesson_ids = [l.id for l in lessons]
    
    completed = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == user_id,
        models.UserProgress.lesson_id.in_(lesson_ids),
        models.UserProgress.completed == True
    ).count()
    
    return {
        "module_id": module_id,
        "total_lessons": len(lessons),
        "completed_lessons": completed,
        "progress_percentage": round((completed / len(lessons) * 100) if lessons else 0, 1)
    }
