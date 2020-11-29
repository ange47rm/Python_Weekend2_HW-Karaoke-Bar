import unittest

from src.karaoke_bar import Karaoke_Bar
from src.guest import Guest
from src.drink import Drink
from src.song import Song

class TestKaraoke_Bar (unittest.TestCase):

    def setUp (self):

        self.karaoke_bar = Karaoke_Bar()

        # SONGS SETUP #
        self.song_1 = Song ("2Pac", "Dear Mama")
        self.song_2 = Song ("The Notorious BIG", "Juicy")
        self.song_3 = Song ("The Midnight", "Los Angeles")

        # GUESTS SETUP #
        self.guest_1 = Guest ("Angelo", 47, self.song_2)
        self.guest_2 = Guest ("Ryan", 128, self.song_3)
        self.guest_3 = Guest ("Sonia", 22, self.song_1)

        # DRINKS SETUP #
        self.drink_1 = Drink ("Coke", 3)
        self.drink_2 = Drink ("Fanta", 3)
        self.drink_3 = Drink ("Beer", 5)
        self.drink_4 = Drink ("Wine", 6)

    def test_karaoke_bar_has_register (self):
        self.assertEqual ({}, self.karaoke_bar.register)

    def test_karaoke_bar_has_list_of_drinks (self):
        self.assertEqual ([], self.karaoke_bar.drinks)

    def test_sell_drink_to_guest (self):
        self.karaoke_bar.sell_drink_to_guest (self.drink_4, self.guest_1)


