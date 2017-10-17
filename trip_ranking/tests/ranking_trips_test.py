"""
Unit Tests for ranking trips module.
"""
import pytest

from trip_ranking.tests.fixtures import sliding_window_rank, dummy_trip_ids, dummy_trips_1, dummy_trips_2
from trip_ranking.trip_ranking import ranking_trips


def test_ranking_trips_sliding_window_rank_dummy_nums():
    arr = dummy_trip_ids()
    assert sliding_window_rank(arr) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]


def test_ranking_trips_less_than_25():
    trips = dummy_trips_1()
    assert ranking_trips.rank_trips(trips) == [2, 7, 4, 9, 6, 12, 8, 13, 14, 18]


def test_ranking_trips_v2_less_than_25():
    trips = dummy_trips_1()
    assert ranking_trips.rank_trips_v2(trips) == [2, 4, 6, 7, 8, 9, 12, 13, 14, 18]


def test_ranking_trips_more_than_25():
    trips = dummy_trips_2()
    assert ranking_trips.rank_trips(trips) == [2, 7, 11, 11, 12, 4, 9, 14, 16, 17, 6, 12, 22, 25, 25, 8, 13, 31, 33, 
        55, 14, 18, 50, 51, 57, 23, 49, 43, 55, 52, 56, 84, 88, 88, 99]