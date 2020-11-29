import unittest

from src.drink import Drink

class TestDrink (unittest.TestCase):

    def setUp (self):

        self.drink_1 = Drink ("Coke", 3)
        self.drink_2 = Drink ("Fanta", 3)
        self.drink_3 = Drink ("Beer", 5)
        self.drink_4 = Drink ("Wine", 6)

    def test_drink_has_name (self):
        self.assertEqual ("Fanta", self.drink_2.name)
