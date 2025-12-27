from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import subprocess
import tempfile
import os
import json
from datetime import datetime

from app.database import get_db
from app.models import User, Lesson, ExerciseSubmission, UserModuleAccess
from app.schemas import ExerciseSubmit, ExerciseResult
from app.routers.auth import require_user

router = APIRouter()


def run_code_safely(code: str, timeout: int = 5):
    """Execute Python code safely and return output"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        temp_path = f.name
    
    try:
        result = subprocess.run(
            ['python', temp_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {"output": "", "error": "Timeout - kod se izvršavao predugo", "success": False}
    except Exception as e:
        return {"output": "", "error": str(e), "success": False}
    finally:
        os.unlink(temp_path)


def check_solution(user_code: str, expected_solution: str, lesson_title: str):
    """Check if user's solution produces expected output"""
    # Run user's code
    user_result = run_code_safely(user_code)
    if not user_result["success"]:
        return {
            "passed": False,
            "output": user_result["output"],
            "error": user_result["error"],
            "expected_output": None
        }
    
    # Run expected solution
    expected_result = run_code_safely(expected_solution)
    expected_output = expected_result["output"].strip()
    user_output = user_result["output"].strip()
    
    # Compare outputs (flexible comparison)
    passed = compare_outputs(user_output, expected_output)
    
    return {
        "passed": passed,
        "output": user_result["output"],
        "error": None,
        "expected_output": expected_output if not passed else None
    }


def compare_outputs(user_output: str, expected_output: str) -> bool:
    """Flexible output comparison"""
    # Exact match
    if user_output == expected_output:
        return True
    
    # Normalize whitespace and compare
    user_lines = [l.strip() for l in user_output.split('\n') if l.strip()]
    expected_lines = [l.strip() for l in expected_output.split('\n') if l.strip()]
    
    if user_lines == expected_lines:
        return True
    
    # Check if user output contains all expected elements
    if all(line in user_output for line in expected_lines):
        return True
    
    # Pattern-based validation for personalized exercises
    # If expected is "Zdravo admin!", accept any "Zdravo <name>!"
    if expected_output.startswith("Zdravo ") and expected_output.endswith("!"):
        if user_output.startswith("Zdravo ") and user_output.endswith("!"):
            return True
    
    return False


@router.post("/submit", response_model=ExerciseResult)
def submit_exercise(
    data: ExerciseSubmit,
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
    
    # Get exercise solution
    if not lesson.exercise_solution:
        raise HTTPException(status_code=400, detail="Ova lekcija nema vježbu")
    
    # Check solution
    result = check_solution(data.code, lesson.exercise_solution, lesson.title)
    
    # Save submission
    submission = ExerciseSubmission(
        user_id=user.id,
        lesson_id=lesson.id,
        exercise_index=data.exercise_index,
        code=data.code,
        output=result["output"],
        passed=result["passed"],
        submitted_at=datetime.utcnow()
    )
    db.add(submission)
    db.commit()
    
    return result


@router.get("/status/{lesson_id}")
def get_exercise_status(
    lesson_id: int,
    user: User = Depends(require_user),
    db: Session = Depends(get_db)
):
    # Get best submission for this lesson
    submission = db.query(ExerciseSubmission).filter(
        ExerciseSubmission.user_id == user.id,
        ExerciseSubmission.lesson_id == lesson_id,
        ExerciseSubmission.passed == True
    ).first()
    
    return {
        "completed": submission is not None,
        "submitted_at": submission.submitted_at if submission else None
    }


@router.get("/history/{lesson_id}")
def get_exercise_history(
    lesson_id: int,
    user: User = Depends(require_user),
    db: Session = Depends(get_db)
):
    submissions = db.query(ExerciseSubmission).filter(
        ExerciseSubmission.user_id == user.id,
        ExerciseSubmission.lesson_id == lesson_id
    ).order_by(ExerciseSubmission.submitted_at.desc()).limit(10).all()
    
    return [{
        "id": s.id,
        "code": s.code,
        "output": s.output,
        "passed": s.passed,
        "submitted_at": s.submitted_at
    } for s in submissions]
