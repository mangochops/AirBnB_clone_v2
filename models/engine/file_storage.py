#!/usr/bin/python3
"""Defines the FileStorage engine"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects
    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp, f)
    
    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    class_name = value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Deletes object from storage dictionary"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
    
    def close(self):
        """Call reload method for deserializing the JSON file to objects"""
        self.reload()

