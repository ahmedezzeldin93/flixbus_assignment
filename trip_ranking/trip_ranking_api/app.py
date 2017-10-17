from flask import Flask, jsonify, request

from trip_ranking.trip_ranking.trips import Trip
from trip_ranking.trip_ranking import ranking_trips

app = Flask(__name__)


@app.route('/rank_trips', methods=['POST'])
def rank_trips_api():
    try:
        payload = request.get_json()
    except Exception as e:
        raise e

    if not payload:
        return bad_request()
    else:
        parsed_trips = payload["trips"]
        trips_to_be_ranked = [Trip(*trip) for trip in parsed_trips]  
        ranked_ids = ranking_trips.rank_trips(trips_to_be_ranked)
        return jsonify({"ranked_trips": ranked_ids})


@app.route('/rank_trips_v2', methods=['POST'])
def rank_trips_api_v2():
    try:
        payload = request.get_json()
    except Exception as e:
        raise e

    if not payload:
        return bad_request()
    else:
        parsed_trips = payload["trips"]
        trips_to_be_ranked = [Trip(*trip) for trip in parsed_trips]  
        ranked_ids = ranking_trips.rank_trips_v2(trips_to_be_ranked)
        return jsonify({"ranked_trips": ranked_ids})



@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + ' Please check data payload',
    }
    response = jsonify(message)
    response.status_code = 400
    return response