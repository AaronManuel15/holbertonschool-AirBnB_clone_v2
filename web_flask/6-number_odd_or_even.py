#!/usr/bin/python3
"""Task 5: Script that starts a Flask web application"""
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """Document"""
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """Document"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Document"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """Document"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>")
def number_text(n):
    """Document"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """Document"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """Document"""
    if n % 2 == 0:
        EorO = "even"
    else:
        EorO = "odd"
    return render_template('6-number_odd_or_even.html', n=n, EorO=EorO)


if __name__ == "__main__":
    """Document"""
    app.run(host="0.0.0.0", port="5000")
