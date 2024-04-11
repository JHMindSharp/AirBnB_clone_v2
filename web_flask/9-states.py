#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display a HTML page with the list of states or specific
    state and its cities"""
    states = storage.all("State")
    if id is not None:
        id = "State." + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
