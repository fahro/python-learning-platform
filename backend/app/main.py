import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import modules, lessons, progress, code_runner
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Python Learning Platform",
    description="Platforma za učenje Pythona kroz 7 modula - 40 časova",
    version="1.0.0"
)

# CORS - allow frontend origins
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins + ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(modules.router, prefix="/api/modules", tags=["Moduli"])
app.include_router(lessons.router, prefix="/api/lessons", tags=["Lekcije"])
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
