#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a rendered html template,
    using the web_static files
    """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    
    return render_template('100-hbnb.html', **locals())
