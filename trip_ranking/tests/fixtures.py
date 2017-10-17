import pytest
import numpy as np
from datetime import datetime

from trip_ranking.trip_ranking.trips import Trip


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


@pytest.fixture
def dummy_trip_ids():
    arr = [list(np.random.choice([1, 2, 3, 4, 5], replace=False, size=5)) for _ in range(5)]
    flat_arr = [item for sublist in arr for item in sublist]
    return flat_arr


@pytest.fixture
def dummy_trips_1():
    trips = [
        Trip(9, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(12, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(13, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(7, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(14, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
        Trip(4, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 30, 50),
        Trip(2, datetime(year=2017, month=10, day=7, hour=12, minute=00), 1, 1, 40, 20),
        Trip(8, datetime(year=2017, month=10, day=8,    hour=12, minute=00), 2, 1, 90, 50),
        Trip(6, datetime(year=2017, month=10, day=8, hour=12, minute=00), 4, 1, 120, 100),
        Trip(18, datetime(year=2017, month=10, day=8, hour=12, minute=00), 2, 1, 120, 50),
    ]
    return trips


@pytest.fixture
def dummy_trips_2():
    trips_2 = [
        Trip(9, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(12, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(13, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(7, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(14, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
        Trip(4, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 30, 50),
        Trip(2, datetime(year=2017, month=10, day=7, hour=12, minute=00), 1, 1, 40, 20),
        Trip(8, datetime(year=2017, month=10, day=8,    hour=12, minute=00), 2, 1, 90, 50),
        Trip(6, datetime(year=2017, month=10, day=8, hour=12, minute=00), 4, 1, 120, 100),
        Trip(18, datetime(year=2017, month=10, day=8, hour=12, minute=00), 2, 1, 120, 50),
        Trip(50, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(11, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(31, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(17, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(22, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
        Trip(25, datetime(year=2017, month=10, day=8, hour=12, minute=00), 2, 1, 120, 50),
        Trip(51, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(12, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(33, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(14, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(25, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
        Trip(16, datetime(year=2017, month=10, day=8, hour=12, minute=00), 2, 1, 120, 50),
        Trip(57, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(11, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(55, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(52, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(88, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
        Trip(84, datetime(year=2017, month=10, day=8, hour=12, minute=00), 2, 1, 120, 50),
        Trip(23, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(43, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(49, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(56, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(88, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
        Trip(55, datetime(year=2017, month=10, day=8, hour=12, minute=00), 2, 1, 120, 50),
        Trip(99, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 110, 60),
        Trip(75, datetime(year=2017, month=10, day=6, hour=12, minute=00), 2, 1, 80, 50),
        Trip(71, datetime(year=2017, month=10, day=6, hour=12, minute=00), 1, 1, 60, 20),
        Trip(79, datetime(year=2017, month=10, day=6, hour=12, minute=00), 3, 1, 60, 30),
        Trip(69, datetime(year=2017, month=10, day=7, hour=12, minute=00), 2, 1, 50, 30),
    ]
    return trips_2
