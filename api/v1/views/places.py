from flask import Flask, jsonify, request, abort
from api.v1.views import app
from models import Place, City, User  # Assuming you have relevant models defined

# Retrieve list of all Place objects of a City
@app.route('/api/v1/cities/<int:city_id>/places', methods=['GET'])
def get_places_by_city(city_id):
    city = City.query.get(city_id)
    if city is None:
        abort(404)  # City not found
    places = city.places
    return jsonify([place.to_dict() for place in places]), 200

# Retrieve a specific Place object
@app.route('/api/v1/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        abort(404)  # Place not found
    return jsonify(place.to_dict()), 200

# Delete a Place object
@app.route('/api/v1/places/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        abort(404)  # Place not found
    return jsonify({}), 200  # Return empty dictionary

# Create a new Place
@app.route('/api/v1/cities/<int:city_id>/places', methods=['POST'])
def create_place(city_id):
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')  # Invalid JSON
    # Check
