#!/usr/bin/python3
"""A simple Flask web application with multiple routes"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a custom message"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display another custom message"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python ' followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n, parity='even')
    else:
        return render_template('6-number_odd_or_even.html', number=n, parity='odd')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)