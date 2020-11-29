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
        self.guest_3 = Guest ("Sonia", 27, self.song_1)
        self.guest_4 = Guest ("Alex", 54, self.song_5)
        self.guest_5 = Guest ("Matt", 176, self.song_6)
        self.guest_6 = Guest ("Lawrence", 85, self.song_4)
        self.guest_7 = Guest ("Luke", 21, self.song_4)

        # ROOMS SETUP # 
        self.room_1 = Room ("Hip-Hop")
        self.room_2 = Room ("Retrowave")

    
        # CLASS METHODS TESTS #
    def test_room_has_music_genre (self):
        self.assertEqual ("Retrowave", self.room_2.music_genre)

    def test_room_has_guest_capacity (self):
        self.assertEqual (5, self.room_1.guest_capacity)

    def test_guest_check_in_and_check_out (self):
        self.room_1.check_in_guest (self.guest_1)
        self.room_1.check_in_guest (self.guest_2)
        self.room_1.check_in_guest (self.guest_3)                       # We have checked in 3 guests in room_1.
        self.assertEqual (3, len(self.room_1.guests))                   # Confirmed 3 checked in guests.
        self.room_1.check_out_guest (self.guest_2)                      # We check out 1 of the 3 guests.
        self.assertEqual (2, len(self.room_1.guests))                   # Guests are now 2, test passed.

    def test_add_and_remove_song_to_room_playlist (self):
        self.room_1.add_song_to_room_playlist (self.song_1)
        self.room_1.add_song_to_room_playlist (self.song_2)             # Added hiphop (2) songs to room_1.
        self.assertEqual (2, len(self.room_1.songs_playlist))           # Confirmed, 2 songs added to playlist.
        self.room_1.remove_song_from_room_playlist (self.song_1)        # Removed 1 song from playlist.
        self.assertEqual (1, len(self.room_1.songs_playlist))           # 1 song in the playlist, test passed.

    def test_clear_music_playlist (self):
        self.room_2.add_song_to_room_playlist (self.song_3)
        self.room_2.add_song_to_room_playlist (self.song_5)
        self.room_2.add_song_to_room_playlist (self.song_7)             # Added retrowave (3) songs to room_2.
        self.assertEqual (3, len(self.room_2.songs_playlist))           # Confirmed, 3 songs added to playlist.
        self.room_2.clear_music_playlist(self.room_2)
        self.assertEqual (0, len(self.room_2.songs_playlist))   

    def test_deny_entry_room_full (self):
        self.room_1.check_in_guest (self.guest_1)
        self.room_1.check_in_guest (self.guest_2)
        self.room_1.check_in_guest (self.guest_3)
        self.room_1.check_in_guest (self.guest_4)                       
        self.room_1.check_in_guest (self.guest_5)                       
        self.assertEqual (5, len(self.room_1.guests))                   # We have checked in 5 guests in room_1. Test passed.
        self.room_1.check_in_guest (self.guest_6)                       # We try to add a 6th guest to the room, however as the room has reached max guest capacity...
        self.assertEqual (5, len(self.room_1.guests))                   # ... the guest was not admitted. Guests are still 5, test passed.

            
    def test_deny_entry_not_enough_money (self):
        self.assertEqual("Guest not allowed in. Room is currently full or guest has not enough money.", self.room_2.check_in_guest (self.guest_7))
        self.assertEqual (0, len(self.room_2.guests))                   # Guest was not allowed in due to insufficient money. Test pass.
    

    

    

    



    



    

