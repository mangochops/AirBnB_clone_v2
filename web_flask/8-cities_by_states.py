#!/usr/bin/python3
"""Module for starting a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

@app.route('/cities_by_states', methods=['GET'])
def cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()



app = Flask(__name__)
app.url_map.strict_slashes = False
