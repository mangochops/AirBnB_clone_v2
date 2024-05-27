from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage, Place, Amenity

@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def get_place_amenities(place_id):
    # Retrieve Place object
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    # Retrieve Amenity objects linked to the Place
    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)

# Implement other API endpoints: DELETE and POST
