import unittest
from battleship.model.ship import Ship


class TestShip(unittest.TestCase):
    def setUp(self):
        self.location = [(0, 0), (0, 1)]
        self.hit = (0, 0)

    def test_init(self):
        self.assertEqual(self.location, Ship(self.location).location)

    def test_hit(self):
        self.assertEqual(1, Ship(self.location).check_hit(self.hit))

    def test_miss(self):
        self.assertEqual(0, Ship(self.location).check_hit((1, 1)))

    def test_sink(self):
        self.assertEqual(2, Ship([self.hit]).check_hit(self.hit))
