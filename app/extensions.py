from flask_pymongo import PyMongo
from flask import jsonify

mongo = PyMongo()

# Function to initialize MongoDB with the URI
def init_extensions(app):
    # Bind the app to PyMongo
    print("init_extentions_call")
    mongo.init_app(app)
    