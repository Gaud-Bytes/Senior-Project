from Boardspace import Boardspace as bs
class Board:
    def __init__(self):
        self._rows, self._cols = (10, 10)
       # self._owner = str(owner)
        self._board = []

        for x in range(self._rows):
            self._board.append([0,0,0,0,0,0,0,0,0,0])
        
        for x in range(self._rows):
            for y in range(self._cols):
                self._board[x][y] = bs()
                self._board[x][y].setCoords(x, y)

                
    def getSpace(self, row, col):
        return self._board[row][col]

    def getRows(self):
        return self._rows

    def getCols(self):
        return self._cols
       

