import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import modules, lessons, progress, code_runner, auth, admin, exercises, quiz
from app.database import engine, Base, SessionLocal
from app.models import User

Base.metadata.create_all(bind=engine)

# Create default admin user
def create_admin():
    db = SessionLocal()
    try:
        admin_user = db.query(User).filter(User.username == "admin").first()
        if not admin_user:
            admin_user = User(username="admin", is_admin=True)
            admin_user.set_password("admin123")
            db.add(admin_user)
            db.commit()
            print("Admin user created: admin / admin123")
    finally:
        db.close()

create_admin()

app = FastAPI(
    title="Python Learning Platform",
    description="Platforma za učenje Pythona kroz 12 modula",
    version="2.0.0"
)

# CORS - allow frontend origins
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173,http://localhost:3123").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins + ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Autentifikacija"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(modules.router, prefix="/api/modules", tags=["Moduli"])
app.include_router(lessons.router, prefix="/api/lessons", tags=["Lekcije"])
app.include_router(exercises.router, prefix="/api/exercises", tags=["Vježbe"])
app.include_router(quiz.router, prefix="/api/quiz", tags=["Kvizovi"])
app.include_router(progress.router, prefix="/api/progress", tags=["Napredak"])
app.include_router(code_runner.router, prefix="/api/code", tags=["Code Runner"])


@app.get("/")
def root():
    return {
        "message": "Python Learning Platform API",
        "docs": "/docs",
        "ukupno_casova": 40,
        "dijelovi": [
            {"naziv": "DIO 1: Osnove i Skripting", "casova": 18},
            {"naziv": "DIO 2: Struktura i Napredne Tehnike", "casova": 22}
        ]
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
