#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self, save_to_disk=False):
    """Returns a dictionary representation of the BaseModel instance."""
    # Get the dictionary representation of the instance
    dict_rep = self.__dict__.copy()
    # Remove the 'password' key if save_to_disk is False
    if not save_to_disk and 'password' in dict_rep:
        del dict_rep['password']
    # Add the class name to the dictionary
    dict_rep['__class__'] = self.__class__.__name__
    # Convert datetime objects to string format
    for key, value in dict_rep.items():
        if isinstance(value, datetime):
            dict_rep[key] = value.isoformat()
    return dict_rep

        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
