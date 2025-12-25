from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Lesson])
def get_all_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).order_by(models.Lesson.module_id, models.Lesson.order).all()


@router.get("/module/{module_id}", response_model=List[schemas.Lesson])
def get_lessons_by_module(module_id: int, db: Session = Depends(get_db)):
    lessons = db.query(models.Lesson).filter(
        models.Lesson.module_id == module_id
    ).order_by(models.Lesson.order).all()
    return lessons


@router.get("/{lesson_id}", response_model=schemas.Lesson)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lekcija nije pronađena")
    return lesson


@router.get("/{lesson_id}/next")
def get_next_lesson(lesson_id: int, db: Session = Depends(get_db)):
    current = db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()
    if not current:
        raise HTTPException(status_code=404, detail="Lekcija nije pronađena")
    
    # Try next in same module
    next_lesson = db.query(models.Lesson).filter(
        models.Lesson.module_id == current.module_id,
        models.Lesson.order > current.order
    ).order_by(models.Lesson.order).first()
    
    if next_lesson:
        return {"next_lesson_id": next_lesson.id, "same_module": True}
    
    # Try first lesson of next module
    current_module = db.query(models.Module).filter(models.Module.id == current.module_id).first()
    next_module = db.query(models.Module).filter(
        models.Module.number > current_module.number
    ).order_by(models.Module.number).first()
    
    if next_module:
        first_lesson = db.query(models.Lesson).filter(
            models.Lesson.module_id == next_module.id
        ).order_by(models.Lesson.order).first()
        if first_lesson:
            return {"next_lesson_id": first_lesson.id, "same_module": False, "new_module": next_module.title}
    
    return {"next_lesson_id": None, "message": "Završili ste sve lekcije!"}
