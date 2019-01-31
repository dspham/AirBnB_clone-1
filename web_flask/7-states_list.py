#!/usr/bin/python3
"""List of states
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a html page of states from the database
    """
    states_list = storage.all("State").values()
    return render_template("7-states_list.html", states_list=states_list)


@app.teardown_appcontext
def teardown_sqlalchemy_session(closed):
    """removes the current SQLAlchemy session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
