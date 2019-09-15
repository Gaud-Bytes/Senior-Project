from Boardspace import Boardspace as bs

class Board:
    _rows, _cols = (10, 10)
    _board = [[0] * _rows] * _cols

    def __init__(self):
        for x in range(len(self._board)):
            for y in range(len(self._board[x])):
                self._board[x][y] = bs()
                self._board[x][y].setCoords(x, y)

                
    def getSpace(self, row, col):
        return self._board[row][col]

    def getRows(self):
        return self._rows

    def getCols(self):
        return self._cols
       

