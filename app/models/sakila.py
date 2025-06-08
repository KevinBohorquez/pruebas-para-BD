# app/models/sakila.py
from sqlalchemy import Column, Integer, String, DateTime, Text, DECIMAL, SMALLINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Actor(Base):
    __tablename__ = "actor"

    actor_id = Column(SMALLINT, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())


class Film(Base):
    __tablename__ = "film"

    film_id = Column(SMALLINT, primary_key=True, autoincrement=True)
    title = Column(String(128), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(SMALLINT, nullable=False)
    rental_duration = Column(SMALLINT, nullable=False, default=3)
    rental_rate = Column(DECIMAL(4, 2), nullable=False, default=4.99)
    length = Column(SMALLINT)
    replacement_cost = Column(DECIMAL(5, 2), nullable=False, default=19.99)
    rating = Column(String(10), default='G')
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(SMALLINT, primary_key=True, autoincrement=True)
    store_id = Column(SMALLINT, nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(50))
    address_id = Column(SMALLINT, nullable=False)
    active = Column(SMALLINT, nullable=False, default=1)
    create_date = Column(DateTime, nullable=False)
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())


class Category(Base):
    __tablename__ = "category"

    category_id = Column(SMALLINT, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    last_update = Column(DateTime, default=func.now(), onupdate=func.now())