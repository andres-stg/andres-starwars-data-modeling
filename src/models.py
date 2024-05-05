import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    subscription_date = Column('date', nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    favPlanets = relationship("FavPlanets")
    

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    movies = Column(String(50))
    mass = Column(Integer)
    favCharacters = relationship("FavCharacters")

class FavCharacters(Base):
    __tablename__ = 'FavCharacters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    character_id = Column(Integer, ForeignKey('Characters.id'))

class FavPlanets(Base):
    __tablename__ = 'FavPlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    planet_id = Column(Integer, ForeignKey('Planets.id'))

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
