import unittest
from src.guest import Guest
from src.room import Room

class TestGuest (unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Dan Moody", 100.00, "Cuddly Toy")

    def test_guest_has_name(self):
        self.assertEqual("Dan Moody", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Cuddly Toy", self.guest.fav_song)

    def test_guest_can_pay_for_entry(self):
        room = Room("Pop", 10.00, 6)
        self.guest.pay_entry(room)
        self.assertEqual(90.00, self.guest.wallet)

    