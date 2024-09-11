from flask import Flask

from .extensions import init_mongo
from .webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # Initialize Extensions (MongoDB)
    mongo=init_mongo(app)
    # Access or create a database
    db = mongo.cx["github_database"]

    # Access or create a collection
    collection = db["github_actions"]   
    
    print(f"Database '{db}' and Collection '{collection}' created successfully")
  
    
    # register blueprints webhook
    app.register_blueprint(webhook)
    
    return app
