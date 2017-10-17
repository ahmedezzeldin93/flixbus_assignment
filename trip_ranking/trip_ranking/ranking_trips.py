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
        five_ranked_ids = fixtures.rank_trips(trips[i:(i + 5)]) if i+5<len(trips) else fixtures.rank_trips(trips[i:])
        trips_ranked_window_five.extend([trips_dict.get(id) for id in five_ranked_ids])    
    
    for i in range(0, len(trips)-5 if len(trips)>25 else len(trips), 25):
        for j in range(i, i+5):
            five_ranked = fixtures.rank_trips(trips_ranked_window_five[j:(j+25):5])
            final_ids_ranked.extend(five_ranked)

    return final_ids_ranked


def rank_trips_v2(trips:List[Trip]) -> List[int]:
    """
    Rank infinite list of trips using customized merge sort.
    :param trips: list of trips.
    :return: list of trip ids.
    """
    if len(trips) < 2:
        return trips
    elif len(trips) <= 5:
        return fixtures.rank_trips(trips)         
    else:
        ranked_trips = merge_sort_trips(trips)
        return [trip.trip_id for trip in ranked_trips]


def merge_sort_trips(trips_list):
    """
    Merge sort algorithm implemented for ranking trips.
    :param trips: list of trips.
    :return: list of trip.
    """
    if len(trips_list) < 2:
        return trips_list
    middle = len(trips_list)//2

    left = merge_sort_trips(trips_list[:middle])
    right = merge_sort_trips(trips_list[middle:])
    return merge(left, right)


def merge(left_list, right_list):
    """
    Merge helper function for merge sort.
    :param trips: list of trips.
    :return: list of trip.
    """
    if not len(left_list) or not len(right_list):
        return left_list or right_list

    result = []
    i, j = 0, 0
    left_trips_dict = {trip.trip_id: trip for trip in left_list}
    right_trips_dict = {trip.trip_id: trip for trip in right_list}
    while (len(result) < len(left_list) + len(right_list)):
        ranked_two_trips_ids = fixtures.rank_trips([left_list[i],right_list[j]])
        # if ids[0] belogs to left, ad the trip of id[0] to result and inc the left
        if ranked_two_trips_ids[0] in left_trips_dict.keys():
            result.append(left_trips_dict[ranked_two_trips_ids[0]])
            i+= 1
        else:
            result.append(right_trips_dict[ranked_two_trips_ids[0]])
            j+= 1
        if i == len(left_list) or j == len(right_list):
            result.extend(left_list[i:] or right_list[j:])
            break 
    return result


