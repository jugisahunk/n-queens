import unittest
from src.nqueens import placequeens

class n_queens_test(unittest.TestCase):
    def test_place_one_queen(self):
        expected_board = [[0],[0]]
        actual_board = placequeens(1)
        self.assertEqual(expected_board, actual_board)

    def test_place_two_queens(self):
        expected_board = [[0,0],[0,0]]
        actual_board = placequeens(2)
        self.assertEqual(expected_board, actual_board)