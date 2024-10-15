import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'))

class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True )
    username = Column(String(50), unique=True, nullable=False)
    firtsname = Column(String(50), nullable=False)
    lastname = Column(String(50))
    email = Column(String(150), unique=True, nullable=False)
    

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3800))
    image = Column(String(250)) #Url de la imagen del character
    id_character = Column(Integer, ForeignKey('favorites.id'))
    Favorite = relationship(Favorite)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3800))
    image = Column(String(250)) #Url de la imagen del character
    id_planet = Column(Integer, ForeignKey('favorites.id'))
    Favorite = relationship(Favorite)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3800))
    image = Column(String(250)) #Url de la imagen del character
    id_vehicle = Column(Integer, ForeignKey('favorites.id'))
    Favorite = relationship(Favorite)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
