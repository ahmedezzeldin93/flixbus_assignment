"""
Trip class
"""
from datetime import datetime


class Trip:
    """
    Class that defines a trip.
    """
    def __init__(self, trip_id, departure_time, trip_time, num_connections, trip_distance, trip_price):
        self.trip_id = trip_id
        
        if isinstance(departure_time, list):
            year, month, day, hour, minute = departure_time
            self.departure_time  = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        elif isinstance(departure_time, datetime):
            self.departure_time = departure_time
        else:
            self.departure_time = None
        self.trip_time = trip_time
        self.num_connections = num_connections
        self.trip_distance = trip_distance
        self.trip_price = trip_price
    
    def __repr__(self):
        return "Trip {}: {}".format(str(self.trip_id), str(self.departure_time))

    def __str__(self):
        return "Trip {}: {}".format(str(self.trip_id), str(self.departure_time))

