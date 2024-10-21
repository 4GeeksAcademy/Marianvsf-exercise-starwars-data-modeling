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
    id_character = Column(Integer, ForeignKey('favoritecharacters.id'))
    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3800))
    image = Column(String(250)) #Url de la imagen del character
    id_planet = Column(Integer, ForeignKey('favoriteplanets.id'))
    

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    caption = Column(String(3800))
    image = Column(String(250)) #Url de la imagen del character
    id_vehicle = Column(Integer, ForeignKey('favaritevehicles.id'))
    

class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('favorites.id'))
    character = relationship(Character)
    

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.id
    

class FavoriteVehicle(Base):
    __tablename__ = 'favoritevehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    user_id = Column(Integer, ForeignKey('favorites.id'))
    vehicle = relationship(Vehicle)
    
    
    def __repr__(self):
        return '<FavoriteVehicle %r>' % self.id
    
class FavoritePlanet(Base):
    __tablename__ = 'favoriteplanets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('favorites.id'))
    planet = relationship(Planet)
    
    
    def __repr__(self):
        return '<FavoritePlanet %r>' % self.id

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
