import unittest
from battleship import server


class TestServer(unittest.TestCase):

    def test_own_board(self):
        expected = 'my own board'
        result = server.own_board()
        self.assertEqual(type(expected), type(result))
        self.assertEqual(expected, result)

    def test_opponent_baord(self):
        expected = 'their board yo'
        result = server.opponent_board()
        self.assertEqual(type(expected), type(result))
        self.assertEqual(expected, result)
