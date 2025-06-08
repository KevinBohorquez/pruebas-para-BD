# app/schemas/sakila.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ActorBase(BaseModel):
    first_name: str
    last_name: str


class Actor(ActorBase):
    actor_id: int
    last_update: datetime

    class Config:
        from_attributes = True


class FilmBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None
    length: Optional[int] = None
    rating: Optional[str] = "G"


class Film(FilmBase):
    film_id: int
    rental_rate: float
    replacement_cost: float
    last_update: datetime

    class Config:
        from_attributes = True


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None


class Customer(CustomerBase):
    customer_id: int
    store_id: int
    active: int
    create_date: datetime
    last_update: datetime

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    category_id: int
    last_update: datetime

    class Config:
        from_attributes = True