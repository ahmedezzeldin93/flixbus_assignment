from flask import Flask, jsonify, request

from trip_ranking.trip_ranking import ranking_trips

app = Flask(__name__)


@app.route('/rank_trips', methods=['POST'])
def rank_trips_api():
    try:
        payload = request.get_json()
    except Exception as e:
        raise e

    if payload.empty:
        return (bad_request())
    else:
        ranked_ids = ranking_trips.rank_trips(payload)
        return ranked_ids


@app.errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + 'Please check data payload',
    }
    response = jsonify(message)
    response.status_code = 400
    return response