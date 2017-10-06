"""
Main module that ranks the trips using the ready made ranking lib.
"""
from typing import List

from trip_ranking.trip_ranking.trips import Trip
from trip_ranking.tests import fixtures


def rank_trips(trips:List[Trip]) -> List[int]:
    """
    Rank infinite list of trips using lib trip rank.
    :param trips: list of trips.
    :return: list of trip ids.
    """
    trips_dict = {trip.trip_id: trip for trip in trips}

    trips_ranked_window_five = []
    final_ids_ranked = []
    for i in range(0, len(trips) - 4, 5):
        five_ranked_ids = fixtures.rank_trips(trips[i:(i + 5)])
        trips_ranked_window_five.extend([trips_dict.get(id) for id in five_ranked_ids])

    for i in range(0, len(trips) // 5):
        five_ranked = fixtures.rank_trips(trips_ranked_window_five[i::5])
        final_ids_ranked.extend(five_ranked)
    return final_ids_ranked
