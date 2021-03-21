import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom (unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Pop", 12.00, 4)
        self.room_2 = Room("Rock", 10.00, 6)
        self.room_3 = Room("Country", 10.00, 6)
        self.guest_1 = Guest("Alan Partridge", 80.00, "Cuddly Toy")
        self.guest_2 = Guest("Dan Moody", 100.00, "Let's Get It On")
        self.guest_3  = Guest("Geordie Michael", 60.00, "Back in the USSR")
        self.guest_4 = Guest("Tex", 60.00, "Whiskey In The Jar")
        self.guest_5 = Guest("Lynn Benfield", 120.00, "9 to 5")
        self.song_1 = Song("Cuddly Toy")
 

    def test_room_has_name(self):
        self.assertEqual("Pop", self.room_1.room_name)

    def test_room_has_entry_fee(self):
        self.assertEqual(12.00, self.room_1.entry_fee)

    def test_room_has_max_capacity(self):
        self.assertEqual(4, self.room_1.max_capacity)

    def test_room_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1, self.room_1)
        self.room_2.check_in_guest(self.guest_2, self.room_2)
        self.assertIn("Alan Partridge", self.room_1.guest_list)
        self.assertIn("Dan Moody", self.room_2.guest_list)

    def test_room_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1, self.room_1)
        self.room_1.check_in_guest(self.guest_2, self.room_1)
        self.room_1.check_out_guest(self.guest_2, self.room_1)
        self.assertIn("Alan Partridge", self.room_1.guest_list)

    def test_can_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1, self.room_1)
        self.assertIn("Cuddly Toy", self.room_1.song_list)

    def test_room_will_reject_guest_when_full(self):
        self.room_1.guest_list = ["Dan Moody", "Alan Partridge", "Geordie Michael", "Tex"]
        self.assertEqual("Room full", self.room_1.check_in_guest(self.guest_5, self.room_1))

    def test_room_will_accept_guest_when_not_full(self):
        self.room_1.guest_list = ["Dan Moody", "Alan Partridge", "Geordie Michael"]
        self.room_1.check_in_guest(self.guest_4, self.room_1)
        self.assertEqual(["Dan Moody", "Alan Partridge", "Geordie Michael", "Tex"], self.room_1.guest_list)

    def test_fav_song_on_songlist_result_in_Whoo(self):
        self.room_1.song_list = ["Cuddly Toy", "Livin La Vida Loca", "All Rise"]
        self.assertEqual("Whoo!", self.room_1.check_for_fave_song(self.guest_1, self.room_1))

    def test_fav_song_not_on_songlist_result_in_Boo(self):
        self.room_1.song_list = ["Livin La Vida Loca", "All Rise"]
        self.assertEqual("Boo!", self.room_1.check_for_fave_song(self.guest_1, self.room_1))    

   