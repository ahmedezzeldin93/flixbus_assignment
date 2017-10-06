import pytest


@pytest.fixture()
def rank_trips(list_of_trips):
    sorted_trips = sorted(list_of_trips, key=lambda trip: trip.trip_id)
    sorted_trips_ids = [trip.trip_id for trip in sorted_trips]
    return sorted_trips_ids


@pytest.fixture()
def rank_trips_id(trips_ids):
    return sorted(trips_ids)


@pytest.fixture()
def sliding_window_rank(all_trips_ids):
    ranked_five = []
    ranked_final = []
    for i in range(0, len(all_trips_ids) - 4, 5):
        five_ranked = rank_trips_id(all_trips_ids[i:(i + 5)])
        ranked_five.extend(five_ranked)

    for i in range(0, len(all_trips_ids) // 5):
        five_ranked = rank_trips_id(ranked_five[i::5])
        ranked_final.extend(five_ranked)
    return ranked_final