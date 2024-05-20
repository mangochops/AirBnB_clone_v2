#!/usr/bin/python3
"""A simple Flask web application with multiple routes"""

from flask import Flask1-hbnb_route.py

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a custom message"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display another custom message"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
