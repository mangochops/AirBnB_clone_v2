# models/engine/db_storage.py
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    # existing code...

    def close(self):
        """Call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()
