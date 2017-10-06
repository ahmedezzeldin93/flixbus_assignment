"""
Trip class
"""

class Trip:
    """
    Class that defines a trip.
    """
    def __init__(self, trip_id, departure_time, trip_time, num_connections, trip_distance, trip_price):
        self.trip_id = trip_id
        self.departure_time  = departure_time
        self.trip_time = trip_time
        self.num_connections = num_connections
        self.trip_distance = trip_distance
        self.trip_price = trip_price
