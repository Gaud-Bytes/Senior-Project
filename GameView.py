import tkinter
from Board import Board

class GameView:


    def __init__(self):
        pass

    def displayBoards(self, pl : Board(), ai : Board()):
        #pl.getSpace(1, 1).attack()
        for x in range(pl.getRows()):
            for y in range(pl.getCols()):
                print(pl.getSpace(x, y).getCoords(), end = '')
            print()


