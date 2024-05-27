#!/usr/bin/python3
"""DBStorage engine module"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage:
    """DBStorage engine for handling MySQL storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

    def all(self, cls=None):
        """Query all objects from the current database session"""
        if cls:
            return {f'{type(obj).__name__}.{obj.id}': obj for obj in self.__session.query(cls).all()}
        else:
            objs = []
            for c in [State, City]:  # Add all other models here
                objs.extend(self.__session.query(c).all())
            return {f'{type(obj).__name__}.{obj.id}': obj for obj in objs}

    def get(self, cls, id):
        """Retrieve an object by class and id"""
        if cls and id:
            return self.__session.query(cls).get(id)
        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if cls:
            return self.__session.query(cls).count()
        else:
            count = 0
            for c in [State, City]:  # Add all other models here
                count += self.__session.query(c).count()
            return count

    # Other methods omitted for brevity

    def close(self):
        """Remove the session"""
        self.__session.remove()
