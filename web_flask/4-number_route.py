#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python {:s}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number_check(n):
    return "{:d} is a number".format(int(n))

if __name__ == "__main__":
    app.run()
