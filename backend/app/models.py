from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import hashlib


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(256))
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    module_access = relationship("UserModuleAccess", back_populates="user", foreign_keys="[UserModuleAccess.user_id]")
    exercise_submissions = relationship("ExerciseSubmission", back_populates="user")
    quiz_attempts = relationship("QuizAttempt", back_populates="user")
    
    def set_password(self, password):
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()


class UserModuleAccess(Base):
    __tablename__ = "user_module_access"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    module_id = Column(Integer, ForeignKey("modules.id"))
    unlocked = Column(Boolean, default=False)
    unlocked_at = Column(DateTime, default=None)
    unlocked_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    user = relationship("User", back_populates="module_access", foreign_keys=[user_id])
    module = relationship("Module")


class Module(Base):
    __tablename__ = "modules"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True)
    title = Column(String(200))
    description = Column(Text)
    duration_hours = Column(Integer)
    part = Column(Integer)  # DIO 1 ili DIO 2
    
    lessons = relationship("Lesson", back_populates="module")


class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, ForeignKey("modules.id"))
    title = Column(String(200))
    content = Column(Text)
    code_example = Column(Text)
    exercise = Column(Text)
    exercise_solution = Column(Text)
    quiz = Column(Text)  # JSON string with quiz questions
    order = Column(Integer)
    duration_hours = Column(Integer, default=1)
    
    module = relationship("Module", back_populates="lessons")


class UserProgress(Base):
    __tablename__ = "user_progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    completed = Column(Boolean, default=False)
    code_submission = Column(Text)
    completed_at = Column(DateTime, default=None)
    
    lesson = relationship("Lesson")


class CodeSubmission(Base):
    __tablename__ = "code_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    code = Column(Text)
    output = Column(Text)
    is_correct = Column(Boolean, default=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)


class ExerciseSubmission(Base):
    __tablename__ = "exercise_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    exercise_index = Column(Integer, default=0)  # Which exercise in the lesson
    code = Column(Text)
    output = Column(Text)
    passed = Column(Boolean, default=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="exercise_submissions")
    lesson = relationship("Lesson")


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    answers = Column(Text)  # JSON string of user answers
    score = Column(Float)  # Percentage score
    passed = Column(Boolean, default=False)  # 70% required
    attempted_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="quiz_attempts")
    lesson = relationship("Lesson")
