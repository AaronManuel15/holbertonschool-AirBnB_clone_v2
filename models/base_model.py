#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from email.policy import default
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60),
                unique=True,
                nullable=False,
                primary_key=True
                )
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime,
                        nullable=False,
                        default=created_at)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.now()
                self.updated_at = self.created_at

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        if getenv("HBNB_TYPE_STORAGE") != 'db':
            if self.__dict__.get('_sa_instance_state'):
                del self.__dict__['_sa_instance_state']

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        # self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get('_sa_instance_state'):
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes current instance from storage"""
        from models import storage
        storage.delete(self)
