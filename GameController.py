from GameModel import GameModel as gm
from GameView import GameView as gv
from tkinter import *

class GameController:

    def __init__(self):
        self._root = Tk()
        self._model = gm()
        self._view = gv(self._root)

    
    def clickSpace(self, event):
        
        coords = self.pixToGridCoord(event.x, event.y)

        if(coords == (-1, -1)):
            return False
        
        if(self._model.yourTurn() and not self._model.isShipPlacementPhase()):
            self._model.getAIBoard().getSpace(coords[0], coords[1]).toggleSelect()
        elif(self._model.isShipPlacementPhase()):
            self._model.getPlayerBoard().getSpace(coords[0], coords[1]).toggleSelect()

        print(coords)

        self.updateView()

    def pixToGridCoord(self, xPix, yPix):
        x1, y1, x2, y2 = (180, 10, 225, 55)
        xCoord, yCoord = (-1, -1)
        yDiff = y2 - y1
        xDiff = x2 - x1
        yMax = yDiff * self._model.getPlayerBoard().getRows() + y2
        xMax = xDiff * self._model.getPlayerBoard().getCols() + x2

        if(xPix > x1 and xPix < xMax) and (yPix > y1 and yPix < yMax ):
            for i in range(self._model.getPlayerBoard().getRows()):
                y1, y2 = (10, 55)
                if(xPix > x1 and xPix < x2):
                        xCoord = i
                for j in range(self._model.getPlayerBoard().getCols()):
                    if (yPix > y1 and yPix < y2):
                        yCoord = j
                    
                    y1 += yDiff
                    y2 += yDiff

                x1 += xDiff
                x2 += xDiff

        return (xCoord, yCoord)
        
    def updateView(self):
        self._view.displayBoards(self._model)
        self._view.getCanvasWidget().bind("<Button-1>", self.clickSpace)

        self._view.displayButtons(self._model.getPlayerShips())
        self._view.displayAIShipList(self._model.getAIShips())

gc = GameController()

gc.updateView()

mainloop()
