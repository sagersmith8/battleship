import unittest
from batteship import main


class TestMain(unittest.TestCase):
    def test_hello(self):
        expected = 'Welcome to battleship'
        result = main.hello()
        self.assertEqual(type(expected), type(result))
        self.assertEqual(expected, result)

    def test_own_board(self):
        expected = 'my own board'
        result = main.own_board()
        self.assertEqual(type(expected), type(result))
        self.assertEqual(expected, result)

    def test_opponent_baord(self):
        expected = 'their board yo'
        result = main.opponent_board()
        self.assertEqual(type(expected), type(result))
        self.assertEqual(expected, result)
