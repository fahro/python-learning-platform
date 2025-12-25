from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


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
