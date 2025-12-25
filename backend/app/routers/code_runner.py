from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import subprocess
import tempfile
import time
import os
from app.database import get_db
from app import models, schemas

router = APIRouter()

FORBIDDEN_IMPORTS = [
    'os.system', 'subprocess', 'eval', 'exec', '__import__',
    'open(', 'file(', 'input(', 'raw_input'
]

ALLOWED_MODULES = [
    'math', 'random', 'datetime', 'json', 'collections',
    'itertools', 'functools', 'operator', 'string', 're',
    'statistics', 'decimal', 'fractions', 'copy', 'pprint'
]


def is_safe_code(code: str) -> tuple[bool, str]:
    code_lower = code.lower()
    for forbidden in FORBIDDEN_IMPORTS:
        if forbidden.lower() in code_lower:
            return False, f"Zabranjeno korištenje: {forbidden}"
    return True, ""


@router.post("/execute", response_model=schemas.CodeExecuteResponse)
def execute_code(request: schemas.CodeExecuteRequest, db: Session = Depends(get_db)):
    # Security check
    is_safe, message = is_safe_code(request.code)
    if not is_safe:
        return schemas.CodeExecuteResponse(
            output="",
            error=f"Sigurnosna greška: {message}",
            execution_time=0,
            is_correct=False
        )
    
    # Create temp file and execute
    start_time = time.time()
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(request.code)
            temp_file = f.name
        
        result = subprocess.run(
            ['python', temp_file],
            capture_output=True,
            text=True,
            timeout=5,
            env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}
        )
        
        execution_time = time.time() - start_time
        
        output = result.stdout
        error = result.stderr if result.returncode != 0 else None
        
        # Check if correct (if lesson_id provided)
        is_correct = None
        if request.lesson_id:
            lesson = db.query(models.Lesson).filter(
                models.Lesson.id == request.lesson_id
            ).first()
            if lesson and lesson.exercise_solution:
                # Simple check - compare output
                expected_output = execute_solution(lesson.exercise_solution)
                is_correct = output.strip() == expected_output.strip()
        
        # Save submission
        if request.user_id and request.lesson_id:
            submission = models.CodeSubmission(
                user_id=request.user_id,
                lesson_id=request.lesson_id,
                code=request.code,
                output=output,
                is_correct=is_correct or False
            )
            db.add(submission)
            db.commit()
        
        return schemas.CodeExecuteResponse(
            output=output,
            error=error,
            execution_time=round(execution_time, 3),
            is_correct=is_correct
        )
        
    except subprocess.TimeoutExpired:
        return schemas.CodeExecuteResponse(
            output="",
            error="Timeout: Kod se izvršavao predugo (max 5 sekundi)",
            execution_time=5.0,
            is_correct=False
        )
    except Exception as e:
        return schemas.CodeExecuteResponse(
            output="",
            error=f"Greška: {str(e)}",
            execution_time=0,
            is_correct=False
        )
    finally:
        if 'temp_file' in locals():
            try:
                os.unlink(temp_file)
            except:
                pass


def execute_solution(code: str) -> str:
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        result = subprocess.run(
            ['python', temp_file],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except:
        return ""
    finally:
        if 'temp_file' in locals():
            try:
                os.unlink(temp_file)
            except:
                pass


@router.get("/submissions/{user_id}")
def get_user_submissions(user_id: str, db: Session = Depends(get_db)):
    submissions = db.query(models.CodeSubmission).filter(
        models.CodeSubmission.user_id == user_id
    ).order_by(models.CodeSubmission.submitted_at.desc()).limit(50).all()
    
    return [
        {
            "id": s.id,
            "lesson_id": s.lesson_id,
            "code": s.code[:200] + "..." if len(s.code) > 200 else s.code,
            "is_correct": s.is_correct,
            "submitted_at": s.submitted_at
        }
        for s in submissions
    ]
