"""
Unit Tests for ranking trips module.
"""
import pytest
import numpy as np
from datetime import datetime

from trip_ranking.trip_ranking.trips import Trip
from trip_ranking.tests.fixtures import sliding_window_rank
from trip_ranking.trip_ranking import ranking_trips


@pytest.fixture
def dummy_trip_ids():
    arr = [list(np.random.choice([1, 2, 3, 4, 5], replace=False, size=5)) for _ in range(5)]
    flat_arr = [item for sublist in arr for item in sublist]
    return flat_arr


@pytest.fixture
def dummy_trips():
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


def test_ranking_trips_sliding_window_rank_dummy_nums():
    arr = dummy_trip_ids()
    assert sliding_window_rank(arr) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]


def test_ranking_trips():
    trips = dummy_trips()
    assert ranking_trips.rank_trips(trips) == [2, 4, 6, 7, 8, 9, 12, 13, 14, 18]
