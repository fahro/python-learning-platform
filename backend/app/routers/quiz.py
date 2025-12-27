from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
from datetime import datetime

from app.database import get_db
from app.models import User, Lesson, QuizAttempt, UserModuleAccess
from app.schemas import QuizSubmit, QuizResult
from app.routers.auth import require_user

router = APIRouter()

PASS_THRESHOLD = 0.70  # 70% required to pass


@router.post("/submit", response_model=QuizResult)
def submit_quiz(
    data: QuizSubmit,
    user: User = Depends(require_user),
    db: Session = Depends(get_db)
):
    # Get lesson
    lesson = db.query(Lesson).filter(Lesson.id == data.lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lekcija nije pronađena")
    
    # Check if user has access to this module
    access = db.query(UserModuleAccess).filter(
        UserModuleAccess.user_id == user.id,
        UserModuleAccess.module_id == lesson.module_id,
        UserModuleAccess.unlocked == True
    ).first()
    
    if not access:
        raise HTTPException(status_code=403, detail="Nemate pristup ovom modulu")
    
    # Parse quiz questions
    if not lesson.quiz:
        raise HTTPException(status_code=400, detail="Ova lekcija nema kviz")
    
    try:
        questions = json.loads(lesson.quiz)
    except:
        raise HTTPException(status_code=500, detail="Greška pri parsiranju kviza")
    
    if len(data.answers) != len(questions):
        raise HTTPException(status_code=400, detail=f"Očekivano {len(questions)} odgovora, dobijeno {len(data.answers)}")
    
    # Grade quiz
    correct_count = 0
    details = []
    
    for i, (question, answer) in enumerate(zip(questions, data.answers)):
        is_correct = answer == question["correct"]
        if is_correct:
            correct_count += 1
        
        details.append({
            "question": question["question"],
            "your_answer": answer,
            "correct_answer": question["correct"],
            "is_correct": is_correct
        })
    
    total_count = len(questions)
    score = (correct_count / total_count) * 100 if total_count > 0 else 0
    passed = score >= (PASS_THRESHOLD * 100)
    
    # Save attempt
    attempt = QuizAttempt(
        user_id=user.id,
        lesson_id=lesson.id,
        answers=json.dumps(data.answers),
        score=score,
        passed=passed,
        attempted_at=datetime.utcnow()
    )
    db.add(attempt)
    db.commit()
    
    return {
        "score": score,
        "passed": passed,
        "correct_count": correct_count,
        "total_count": total_count,
        "details": details
    }


@router.get("/status/{lesson_id}")
def get_quiz_status(
    lesson_id: int,
    user: User = Depends(require_user),
    db: Session = Depends(get_db)
):
    # Get best attempt for this lesson
    best_attempt = db.query(QuizAttempt).filter(
        QuizAttempt.user_id == user.id,
        QuizAttempt.lesson_id == lesson_id
    ).order_by(QuizAttempt.score.desc()).first()
    
    passed_attempt = db.query(QuizAttempt).filter(
        QuizAttempt.user_id == user.id,
        QuizAttempt.lesson_id == lesson_id,
        QuizAttempt.passed == True
    ).first()
    
    return {
        "attempted": best_attempt is not None,
        "passed": passed_attempt is not None,
        "best_score": best_attempt.score if best_attempt else None,
        "attempts_count": db.query(QuizAttempt).filter(
            QuizAttempt.user_id == user.id,
            QuizAttempt.lesson_id == lesson_id
        ).count()
    }


@router.get("/history/{lesson_id}")
def get_quiz_history(
    lesson_id: int,
    user: User = Depends(require_user),
    db: Session = Depends(get_db)
):
    attempts = db.query(QuizAttempt).filter(
        QuizAttempt.user_id == user.id,
        QuizAttempt.lesson_id == lesson_id
    ).order_by(QuizAttempt.attempted_at.desc()).limit(10).all()
    
    return [{
        "id": a.id,
        "score": a.score,
        "passed": a.passed,
        "attempted_at": a.attempted_at
    } for a in attempts]
