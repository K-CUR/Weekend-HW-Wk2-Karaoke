import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom (unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Pop", 10.00, 6)
        self.room_2 = Room("Rock", 10.00, 6)
        self.room_3 = Room("Country", 10.00, 8)
        self.guest_1 = Guest("Dan Moody", 100.00, "Cuddly Toy")
        self.guest_2 = Guest("Tex", 60.00, "Whiskey In The Jar")
        self.guest_3 = Guest("Lynn Benfield", 120.00, "9 to 5")
        self.song_1 = Song("Cuddly Toy")
        self.song_2 = Song("Sharp Dressed Man")
        self.song_3 = Song("Drivin My Life Away")
        self.guest_list = []

    def test_room_has_name(self):
        self.assertEqual("Pop", self.room_1.room_name)

    def test_room_has_entry_fee(self):
        self.assertEqual(10.00, self.room_1.entry_fee)

    def test_room_has_max_capacity(self):
        self.assertEqual(6, self.room_1.max_capacity)

    def test_room_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1, self.room_1)
        self.room_2.check_in_guest(self.guest_2, self.room_2)
        self.assertIn("Dan Moody", self.room_1.guest_list)
        self.assertIn("Tex", self.room_2.guest_list)

    def test_room_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1, self.room_1)
        self.room_1.check_in_guest(self.guest_2, self.room_1)
        self.room_1.check_out_guest(self.guest_2, self.room_1)
        self.assertIn("Dan Moody", self.room_1.guest_list)

    def test_can_add_song_to_room(self):
        self.room_3.add_song_to_room(self.song_3, self.room_3)
        self.assertIn("Drivin My Life Away", self.room_3.song_list) 