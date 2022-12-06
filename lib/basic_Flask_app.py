"""
This is a minimal working Flask example it has one function hello_world() that is bound to the root of the server ('/')
From the flask file the Flask object is imported and a new Flask app objects is created
To run this example uncomment in the file run_app.py the line lib.basic_Flask_app import app
Using a browser and going to the root of the server (http://127.0.0.1:5000/) will access the hello_world() function
"""

from flask import Flask

app = Flask(__name__)


# the @app.route part above the hello_world() function is a helper method from Flask that
# will bind the root ('/') of the server to the hello_world() view function
@app.route('/')
def hello_world():
    # it does nothing more than returning a string to the outside world to view
    return 'Hello World!'


# TODO
# add a new view function that will be bound to the address /name and will print your name
