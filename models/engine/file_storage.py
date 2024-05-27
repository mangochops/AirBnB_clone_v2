#!/usr/bin/python3
"""FileStorage engine module"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
import os

class FileStorage:
    """FileStorage engine for handling JSON storage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary of objects"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def get(self, cls, id):
        """Retrieve an object by class and id"""
        key = f'{cls.__name__}.{id}'
        return self.__objects.get(key, None)

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if cls:
            return len(self.all(cls))
        return len(self.__objects)

    # Other methods omitted for brevity
