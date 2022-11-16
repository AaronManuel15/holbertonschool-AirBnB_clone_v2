#!/usr/bin/python3
"""Task 9: Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', sorted_states=states)


@app.teardown_appcontext
def app_teardown(arg):
    """Document"""
    storage.close()


if __name__ == "__main__":
    """Document"""
    app.run(host="0.0.0.0", port="5000")
