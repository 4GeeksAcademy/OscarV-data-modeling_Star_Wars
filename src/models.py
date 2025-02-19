import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

#python src/models.py

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname= Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    date_join = Column(DateTime)

class Planets(Base):
    __tablename__ = 'planets'
    id_planet= Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate= Column(String(250), nullable=False)
    terrain= Column(String(250), nullable=False)
    population= Column(Integer, nullable=False)

class People(Base):
    __tablename__ = 'people'
    id_people = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color= Column(String(250), nullable=False)
    skin_color= Column(String(250), nullable=False)
    eye_color= Column(String(250), nullable=False)
    birth_year= Column(String(250), nullable=False)
    gender= Column(String(250), nullable=False)
    id_homeworld = Column(Integer, ForeignKey('planets.id_planet'))
    planets = relationship(Planets)    

class Favorites(Base):
    __tablename__ = 'favorites'
    id_favorites = Column(Integer, primary_key=True)
    date_favorites = Column(DateTime)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)   
    id_people = Column(Integer, ForeignKey('people.id_people'))
    people = relationship(People) 
    id_planets = Column(Integer, ForeignKey('planets.id_planet'))
    planets = relationship(Planets)
    

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
