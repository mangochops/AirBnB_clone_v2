#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    @property
    def cities(self):
        """Returns the list of City objects from storage linked to the current State"""
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        return self.cities  # SQLAlchemy relationship attribute
