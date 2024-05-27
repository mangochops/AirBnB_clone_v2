import hashlib
from models.base_model import BaseModel
 
"""This module defines a class User"""
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialize User object."""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """Getter method for password."""
        return self.__password

    @password.setter
    def password(self, value):
        """Setter method for password, hashes the password to MD5."""
        md5_hash = hashlib.md5(value.encode()).hexdigest()
        self.__password = md5_hash
   
    
    
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
