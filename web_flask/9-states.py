#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

@app.route('/states', methods=['GET'])
def states_list():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', methods=['GET'])
def state_cities(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

app = Flask(__name__)
app.url_map.strict_slashes = False
