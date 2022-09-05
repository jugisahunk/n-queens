import unittest
from src.nqueens import placequeens

class n_queens_test(unittest.TestCase):
    def pretty_print_board(self, board):    
        print('print board')
        print(board)    
        for row in board:
            print(''.join(row))
    
    def test_place_one_queen(self):
        expected_board = [['X']]
        actual_board = placequeens(1)
        self.assertEqual(expected_board, actual_board)

    def test_place_two_queens(self):
        rows = []
        expected_board = [['X','X'],['X','X']]
        actual_board = placequeens(2)

        self.assertEqual(expected_board, actual_board)

    # def test_place_4_queens(self):
    #     expected_board = [[],[]]]