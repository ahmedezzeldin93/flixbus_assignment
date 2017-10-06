"""
Flask run module.
"""
from trip_ranking.trip_ranking_api.app import app
app.run(debug=True)