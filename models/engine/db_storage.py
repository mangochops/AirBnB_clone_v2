#!/usr/bin/python3
"""Defines the DBStorage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
import os

class DBStorage:
    """DBStorage class for ORM storage"""
    
    __engine = None
    __session = None
    
    def __init__(self):
        """Initialize the DBStorage engine"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')
        
        self.__engine = create_engine(f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}', pool_pre_ping=True)
        
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query all objects depending on the class name"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}
    
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Reloads data from the database"""
        from models.base_model import Base, BaseModel
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """Remove the session"""
        self.__session.remove()
