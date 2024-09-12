from flask import Flask

from .extensions import init_extensions
from .webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    app.config["MONGO_URI"] = "mongodb+srv://vaskar:jSksNkXmABog6wkI@cluster0.e2yil.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    init_extensions(app)
    
    # register blueprints webhook
    app.register_blueprint(webhook)
    
    return app
