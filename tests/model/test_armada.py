import unittest
import os
from battleship.model.armada import Armada


class TestArmada(unittest.TestCase):
    def setUp(self):
        """
        Sets up unit tests for armada
        """
        self.path = os.path.join('resources', 'sample_board.txt')
        self.ships = {
            'B': [(0, 0), (0, 1), (0, 2)],
            'D': [(0, 3), (0, 4), (0, 5)],
            'R': [(0, 6), (0, 7), (0, 8)]
        }

    def test_init(self):
        """
        Tests init for armada
        """
        armada = Armada(self.path)
        self.assertEqual(armada.ships.keys(), self.ships.keys())

        for ship in self.ships:
            print armada.ships.get(ship).location
            self.assertEqual(
                armada.ships.get(ship).location,
                self.ships.get(ship)
            )

    def test_miss(self):
        """
        Tests that an armada isn't always hit
        """
        armada = Armada(self.path)
        self.assertEqual(0, armada.check_hit((5, 5)))
        self.assertEqual(3, len(armada.ships))

    def test_hit(self):
        """
        Tests that a ship is hit, but can't be hit twice at the same point
        """
        armada = Armada(self.path)
        self.assertEqual(1, armada.check_hit((0, 0)))
        self.assertEqual(0, armada.check_hit((0, 0)))
        self.assertEqual(3, len(armada.ships))

    def test_sink(self):
        """
        Tests that a ship can sink and that once it does it is removed
        from the armada
        """
        armada = Armada(self.path)
        self.assertEqual(1, armada.check_hit((0, 0)))
        self.assertEqual(3, len(armada.ships))
        self.assertEqual(1, armada.check_hit((0, 1)))
        self.assertEqual(3, len(armada.ships))
        self.assertEqual('B', armada.check_hit((0, 2)))
        self.assertEqual(2, len(armada.ships))
