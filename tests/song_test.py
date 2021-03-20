import unittest
from src.song import Song

class TestSong (unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Cuddly Toy")
    # self is used to represent an instance of the class.

    def test_song_has_title(self):
        self.assertEqual("Cuddly Toy", self.song_1.title)