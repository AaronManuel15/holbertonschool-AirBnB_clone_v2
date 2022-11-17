#!/usr/bin/python3
"""Task 11: Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """Documents"""
    states = storage.all(State)
    amenityList = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenityList=amenityList)


@app.teardown_appcontext
def app_teardown(arg):
    """Document"""
    storage.close()


if __name__ == "__main__":
    """Document"""
    app.run(host="0.0.0.0", port="5000")
