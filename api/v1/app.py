#!/usr/bin/python3
"""Module for setting up the Flask application"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

# Create CORS instance
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors and returns a JSON response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
