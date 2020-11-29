import unittest

from src.guest import Guest
from src.song import Song

class TestGuest (unittest.TestCase):
    
    def setUp (self):
        
        # SONGS SETUP #
        self.song_1 = Song ("2Pac", "Dear Mama")
        self.song_2 = Song ("The Notorious BIG", "Juicy")
        self.song_3 = Song ("The Midnight", "Los Angeles")

        # GUESTS SETUP #
        self.guest_1 = Guest ("Angelo", 47, self.song_2)
        self.guest_2 = Guest ("Ryan", 128, self.song_3)
        self.guest_3 = Guest ("Sonia", 22, self.song_1)

    
    def test_guest_has_name (self):
        self.assertEqual ("Sonia", self.guest_3.name)

    def test_guest_has_money (self):
        self.assertEqual (128, self.guest_2.money)
        
    def test_guest_has_fave_song(self):
        self.assertEqual (("The Notorious BIG", "Juicy"), (self.guest_1.song.artist, self.guest_1.song.title))



    