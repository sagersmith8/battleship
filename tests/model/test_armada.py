import unittest
import os
from battleship.model.armada import Armada


class TestArmada(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join('resources', 'sample_board.txt')
        self.ships = {
            'B': [(0, 0), (0, 1), (0, 2)],
            'D': [(0, 3), (0, 4), (0, 5)],
            'R': [(0, 6), (0, 7), (0, 8)]
        }

    def test_init(self):
        armada = Armada(self.path)
        self.assertEqual(armada.ships.keys(), self.ships.keys())

        for ship in self.ships:
            print armada.ships.get(ship).location
            self.assertEqual(
                armada.ships.get(ship).location,
                self.ships.get(ship)
            )

    def test_check_hit(self):
        armada = Armada(self.path)
        misses = [(x, y) for x in range(9) for y in range(9)]
        for l in self.ships.values():
            for val in l:
                print val
                misses.remove(val)
                self.assertTrue(str(armada.check_hit(val)) in '01BDRCS')
        for miss in misses:
            self.assertEqual(0, armada.check_hit(miss))
