# app/main.py (VERSIÓN MEJORADA)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Veterinaria API",
    version="1.0.0",
    description="API para sistema veterinario"
)

# Configurar CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://*.railway.app",  # Permitir subdominios Railway
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "🏥 API Veterinaria funcionando!",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "veterinaria-api",
        "environment": os.getenv("ENVIRONMENT", "unknown")
    }

@app.get("/info")
async def info():
    return {
        "name": os.getenv("PROJECT_NAME", "Veterinaria API"),
        "version": os.getenv("VERSION", "1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "production")
    }