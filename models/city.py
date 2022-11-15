#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    storageType = getenv("HBNB_TYPE_STORAGE")
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if storageType == 'db':
        places = relationship('Place',
                              cascade="all, delete, delete-orphan",
                              backref='cities')
