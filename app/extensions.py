from flask_pymongo import PyMongo

mongo = PyMongo()

# Function to initialize MongoDB with the URI
def init_mongo(app):
    app.config["MONGO_URI"] = "mongodb+srv://vaskar:jSksNkXmABog6wkI@cluster0.e2yil.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    mongo.init_app(app)
    try:
        client =mongo.cx
        
        # client.server_info()
        print("MongoDB connection successful")
    except Exception as e:
        print(f"An error occurred: {e}")
    return mongo