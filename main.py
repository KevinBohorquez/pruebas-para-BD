# main.py (VERSIÓN CON SAKILA)
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os

# Importar modelos y esquemas
from app.config.database import get_db
from app.models.sakila import Actor, Film, Customer, Category
from app.schemas.sakila import Actor as ActorSchema, Film as FilmSchema, Customer as CustomerSchema, Category as CategorySchema

app = FastAPI(
    title="Veterinaria API con Sakila",
    version="1.0.0",
    description="API para sistema veterinario + Base de datos Sakila de ejemplo"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================
# ENDPOINTS ORIGINALES
# ================================

@app.get("/")
async def root():
    return {
        "message": "🏥 API Veterinaria con Sakila funcionando!",
        "environment": os.getenv("ENVIRONMENT", "production"),
        "version": "1.0.0",
        "database": "Sakila MySQL en Railway"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "veterinaria-api",
        "database": "sakila"
    }

# ================================
# ENDPOINTS SAKILA
# ================================

@app.get("/actors", response_model=List[ActorSchema])
async def get_actors(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Obtener lista de actores"""
    actors = db.query(Actor).offset(skip).limit(limit).all()
    return actors

@app.get("/actors/{actor_id}", response_model=ActorSchema)
async def get_actor(actor_id: int, db: Session = Depends(get_db)):
    """Obtener un actor por ID"""
    actor = db.query(Actor).filter(Actor.actor_id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor no encontrado")
    return actor

@app.get("/films", response_model=List[FilmSchema])
async def get_films(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Obtener lista de películas"""
    films = db.query(Film).offset(skip).limit(limit).all()
    return films

@app.get("/films/{film_id}", response_model=FilmSchema)
async def get_film(film_id: int, db: Session = Depends(get_db)):
    """Obtener una película por ID"""
    film = db.query(Film).filter(Film.film_id == film_id).first()
    if film is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return film

@app.get("/customers", response_model=List[CustomerSchema])
async def get_customers(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Obtener lista de clientes"""
    customers = db.query(Customer).offset(skip).limit(limit).all()
    return customers

@app.get("/categories", response_model=List[CategorySchema])
async def get_categories(db: Session = Depends(get_db)):
    """Obtener todas las categorías"""
    categories = db.query(Category).all()
    return categories

@app.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    """Estadísticas de la base de datos Sakila"""
    return {
        "total_actors": db.query(Actor).count(),
        "total_films": db.query(Film).count(),
        "total_customers": db.query(Customer).count(),
        "total_categories": db.query(Category).count()
    }

# Endpoint para probar conexión
@app.get("/test-db")
async def test_database(db: Session = Depends(get_db)):
    """Probar conexión a la base de datos"""
    try:
        # Intentar hacer una query simple
        actor_count = db.query(Actor).count()
        return {
            "status": "success",
            "message": "Conexión a base de datos exitosa",
            "sample_data": f"Total actores: {actor_count}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión: {str(e)}")