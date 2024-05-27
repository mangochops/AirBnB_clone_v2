from flask import Flask, jsonify, request, abort
from api.v1.views import app
from models import User  # Assuming you have a User model defined

# Retrieve list of all User objects
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Retrieve a specific User object
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)  # User not found
    return jsonify(user.to_dict()), 200

# Delete a User object
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)  # User not found
    return jsonify({}), 200  # Return empty dictionary

# Create a new User
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')  # Invalid JSON
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    # Create User object and return it
    new_user = User(email=data['email'], password=data['password'])
    new_user.save()  # Assuming a method to save the user
    return jsonify(new_user.to_dict()), 201

# Update a User object
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)  # User not found
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')  # Invalid JSON
    # Update User object with all key-value pairs of the dictionary
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()  # Assuming a method to save the user
    return jsonify(user.to_dict()), 200
