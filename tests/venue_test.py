import unittest

from src.room import Room
from src.venue import Venue


class TestVenue (unittest.TestCase):
    def setUp(self):
        self.venue = Venue(200.00)
        self.room_1 = Room("Pop", 12.00, 4)
        self.room_2 = Room("Rock", 10.00, 6)
        self.room_3 = Room("Country", 10.00, 6)
        

    def test_venue_has_till(self):
        self.assertEqual(200.00, self.venue.till)

    def test_venue_can_add_entry_to_till(self):
        self.venue.add_entry_to_till(self.room_1)
        self.assertEqual(212.00, self.venue.till)

    