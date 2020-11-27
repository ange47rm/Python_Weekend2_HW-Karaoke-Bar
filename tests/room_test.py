import unittest

from src.guest import Guest 
from src.song import Song 
from src.room import Room 

class TestRoom (unittest.TestCase):
    
    def setUp (self):
        
        # SONGS SETUP #
        self.song_1 = Song ("2Pac", "Dear Mama")
        self.song_2 = Song ("The Notorious BIG", "Juicy")
        self.song_3 = Song ("The Midnight", "Los Angeles")
        self.song_4 = Song ("Wu-Tang", "CREAM")
        self.song_5 = Song ("Kalax", "Fight for us")
        self.song_6 = Song ("Rick Astley", "Never Gonna Give You Up")
        self.song_7 = Song ("Gunship", "Tech Noir")

        # GUESTS SETUP #
        self.guest_1 = Guest ("Angelo", 47, self.song_2)
        self.guest_2 = Guest ("Ryan", 128, self.song_3)
        self.guest_3 = Guest ("Sonia", 22, self.song_1)
        self.guest_4 = Guest ("Alex", 54, self.song_2)
        self.guest_5 = Guest ("Matt", 176, self.song_3)
        self.guest_6 = Guest ("Lawrence", 85, self.song_1)
        self.guest_7 = Guest ("Luke", 21, self.song_1)

        # ROOMS SETUP # 
        self.room_1 = Room ("Hip-Hop", [self.guest_1, self.guest_7, self.guest_4], [self.song_1, self.song_2, self.song_4, self.song_6])
        self.room_2 = Room ("Retrowave", [self.guest_2, self.guest_3, self.guest_5, self.guest_6], [self.song_3, self.song_5, self.song_7])

