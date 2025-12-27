from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# Module Schemas
class LessonBase(BaseModel):
    title: str
    content: str
    code_example: Optional[str] = None
    exercise: Optional[str] = None
    exercise_solution: Optional[str] = None
    quiz: Optional[str] = None
    order: int
    duration_hours: int = 1


class LessonCreate(LessonBase):
    module_id: int


class Lesson(LessonBase):
    id: int
    module_id: int
    
    class Config:
        from_attributes = True


class ModuleBase(BaseModel):
    number: int
    title: str
    description: str
    duration_hours: int
    part: int


class ModuleCreate(ModuleBase):
    pass


class Module(ModuleBase):
    id: int
    lessons: List[Lesson] = []
    
    class Config:
        from_attributes = True


class ModuleSummary(BaseModel):
    id: int
    number: int
    title: str
    duration_hours: int
    part: int
    lesson_count: int
    
    class Config:
        from_attributes = True


# Progress Schemas
class ProgressUpdate(BaseModel):
    user_id: str
    lesson_id: int
    completed: bool
    code_submission: Optional[str] = None


class UserProgressResponse(BaseModel):
    id: int
    user_id: str
    lesson_id: int
    completed: bool
    completed_at: Optional[datetime]
    
    class Config:
        from_attributes = True


class UserStats(BaseModel):
    total_lessons: int
    completed_lessons: int
    progress_percentage: float
    total_hours: int
    completed_hours: int


# Code Runner Schemas
class CodeExecuteRequest(BaseModel):
    code: str
    lesson_id: Optional[int] = None
    user_id: Optional[str] = None


class CodeExecuteResponse(BaseModel):
    output: str
    error: Optional[str] = None
    execution_time: float
    is_correct: Optional[bool] = None


# Auth Schemas
class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    is_admin: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserWithProgress(UserResponse):
    completed_lessons: int = 0
    completed_exercises: int = 0
    passed_quizzes: int = 0
    unlocked_modules: int = 0


# Module Access Schemas
class ModuleAccessUpdate(BaseModel):
    user_id: int
    module_id: int
    unlocked: bool


class ModuleAccessResponse(BaseModel):
    id: int
    user_id: int
    module_id: int
    unlocked: bool
    unlocked_at: Optional[datetime]
    
    class Config:
        from_attributes = True


# Exercise Schemas
class ExerciseSubmit(BaseModel):
    lesson_id: int
    exercise_index: int
    code: str


class ExerciseResult(BaseModel):
    passed: bool
    output: str
    error: Optional[str] = None
    expected_output: Optional[str] = None


# Quiz Schemas
class QuizSubmit(BaseModel):
    lesson_id: int
    answers: List[int]  # List of selected option indices


class QuizResult(BaseModel):
    score: float
    passed: bool
    correct_count: int
    total_count: int
    details: List[dict]  # Question-by-question breakdown


# Admin Schemas
class AdminUserStats(BaseModel):
    user: UserResponse
    modules_unlocked: List[int]
    lessons_completed: int
    exercises_passed: int
    quizzes_passed: int
    last_activity: Optional[datetime]
