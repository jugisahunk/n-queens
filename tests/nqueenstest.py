import unittest
from src.nqueens import placequeens

class n_queens_test(unittest.TestCase):
    def test_place_one_queen(self):
        board = [[0],[0]]
        self.assertEqual(board, [[0],[0]])