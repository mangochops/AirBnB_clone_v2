#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

@app.route('/hbnb_filters', methods=['GET'])
def hbnb_filters():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


app = Flask(__name__)
app.url_map.strict_slashes = False
