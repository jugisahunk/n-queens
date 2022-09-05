def placequeens(n):
    rows, cols = (n, n)

    board = [['X' for i in range(cols)] for j in range(rows)]

    return board