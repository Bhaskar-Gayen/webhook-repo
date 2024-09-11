from flask import Blueprint, request, jsonify
from datetime import datetime
from ..extensions import mongo

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver(): 
    data = request.json
    print(data)
    print(mongo.db)
    
    if data:
        # Access the MongoDB collection and insert the event data
        # events_collection = mongo.db.github_events

        event = {
            "request_id": data["commits"][0]["id"],
            "author_name": data["commits"][0]["author"]["name"],
            "action": "commit",
            "from_branch":  data["before"],
            "to_branch": data["after"],
            "timestamp": datetime.strptime(data["commits"][0]["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
        }
        
        print(event)

        # events_collection.insert_one(event)

        return jsonify({"status": "Webhook data received and stored"}), 200
    else:
        return jsonify({"error": "No data received"}), 400

@webhook.route('/test', methods=["GET"])
def test():
    return {"message":"test"}, 200