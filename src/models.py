import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(20), nullable=False)
    subscription_date = Column('date', nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250), nullable=False)
    favPlanets = relationship(User)

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    movies = Column(String(50))
    mass = Column(Integer)
    

class favCharacters(Base):
    __tablename__ = 'favCharacters'
    id = Column(Integer, primary_key=True)
    favCharacters = relationship(User)
    favCharacters = relationship(Characters)

class favPlanets(Base):
    __tablename__ = 'favPlanets'
    id = Column(Integer, primary_key=True)
    favPlanets = relationship(User)
    favPlanets = relationship(Planets)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
