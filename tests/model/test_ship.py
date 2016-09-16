import unittest
from battleship.model.ship import Ship


class TestShip(unittest.TestCase):
    def setUp(self):
        """
        Sets up the unit tests for ship
        """
        self.location = [(0, 0), (0, 1)]
        self.hit = (0, 0)

    def test_init(self):
        """
        Tests the init funtion of the ship
        """
        self.assertEqual(self.location, Ship(self.location).location)

    def test_hit(self):
        """
        Tests whether a ship can be hit
        """
        ship = Ship(self.location)
        self.assertEqual(self.location, ship.location)
        self.assertEqual(1, ship.check_hit(self.hit))
        self.assertEqual(1, len(ship.location))

    def test_miss(self):
        """
        Tests whether a ship can be sunk
        """
        ship = Ship([self.hit])
        self.assertEqual([self.hit], ship.location)
        self.assertEqual(0, ship.check_hit((1, 1)))
        self.assertEqual(1, len(ship.location))

    def test_sink(self):
        """
        Tests whether a ship can be sunk
        """
        ship = Ship([self.hit])
        self.assertEqual([self.hit], ship.location)
        self.assertEqual(2, ship.check_hit(self.hit))
        self.assertEqual(0, len(ship.location))
