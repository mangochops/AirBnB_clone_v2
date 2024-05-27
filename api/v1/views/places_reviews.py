from flask import Flask, jsonify, request, abort
from api.v1.views import app
from models import Place, Review, User  # Assuming you have relevant models defined

# Retrieve list of all Review objects of a Place
@app.route('/api/v1/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        abort(404)  # Place not found
    reviews = place.reviews
    return jsonify([review.to_dict() for review in reviews]), 200

# Retrieve a specific Review object
@app.route('/api/v1/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if review is None:
        abort(404)  # Review not found
    return jsonify(review.to_dict()), 200

# Delete a Review object
@app.route('/api/v1/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if review is None:
        abort(404)  # Review not found
    return jsonify({}), 200  # Return empty dictionary

# Create a new Review
@app.route('/api/v1/places/<int:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')  # Invalid JSON
    # Check if place_id is linked to a Place object
    place = Place.query.get(place_id)
    if place is None:
        abort(404, 'Place not found')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    # Check if user_id is linked to a User object
    user = User.query.get(data['user_id'])
    if user is None:
        abort(404, 'User not found')
    if 'text' not in data:
        abort(400, 'Missing text')
    # Create Review object and return it
    new_review = Review(text=data['text'], place_id=place_id, user_id=data['user_id'])
    new_review.save()  # Assuming a method to save the review
    return jsonify(new_review.to_dict()), 201

# Update a Review object
@app.route('/api/v1/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if review is None:
        abort(404)  # Review not found
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')  # Invalid JSON
    # Update Review object with all key-value pairs of the dictionary
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()  # Assuming a method to save the review
    return jsonify(review.to_dict()), 200
