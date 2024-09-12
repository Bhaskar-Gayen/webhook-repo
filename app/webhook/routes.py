from flask import Blueprint, request, jsonify
from datetime import datetime
from ..extensions import mongo

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

# events = mongo.db.events
# print(mongo)


@webhook.route('/receiver', methods=["POST"])
def receiver(): 
    
    # Collection reference
    events = mongo.db.events
    
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    
    # Push event
    if event_type == 'push':
        branch = data['ref'].split('/')[-1]
        event = {
            'action': 'push',
            'author': data['pusher']['name'],
            'to_branch': branch,
            'timestamp': datetime.utcnow()
        }
        events.insert_one(event)
        return "Push event received", 200

    # Pull request event
    elif event_type == 'pull_request':
        event = {
            'action': 'pull_request',
            'author': data['pull_request']['user']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': datetime.utcnow()
        }
        events.insert_one(event)
        return "Pull request event received", 200

    # Merge event
    elif event_type == 'pull_request' and data['action'] == 'closed' and data['pull_request']['merged']:
        event = {
            'action': 'merge',
            'author': data['pull_request']['user']['login'],
            'from_branch': data['pull_request']['head']['ref'],
            'to_branch': data['pull_request']['base']['ref'],
            'timestamp': datetime.utcnow()
        }
        events.insert_one(event)
        return "Merge event received", 200

    return "Event not handled", 400

@webhook.route("/events", methods=["GET"])
def get_events():
    latest_events = list(events.find().sort("timestamp", -1).limit(10))
    for event in latest_events:
        event['_id'] = str(event['_id'])  # Convert ObjectId to string
    return jsonify(latest_events)

