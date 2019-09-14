import Boardspace as bs

class Board:
    rows, cols = (10, 10)
    board = [[0] * rows] * cols

    def __init__(self):
        for x in range(rows):
            for y in range(cols):
                board[x][y] = bs()
    
    

