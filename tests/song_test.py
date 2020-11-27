import unittest

from src.song import Song


class TestSong (unittest.TestCase):

    def setUp (self):
        self.song_1 = Song ("Jay Z", "Story of OJ")
        self.song_2 = Song ("Gunship", "Tech Noir")
        self.song_3 = Song ("The Midnight", "Los Angeles")

    def test_song_has_artist (self):
        self.assertEqual ("The Midnight", self.song_3.artist)

    def test_song_has_title (self):
        self.assertEqual ("Tech Noir", self.song_2.title)
