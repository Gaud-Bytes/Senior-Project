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

        print(coords)

        self.updateView()

    def pixToGridCoord(self, xPix, yPix):
        x1, y1, x2, y2 = (10, 10, 45, 45)
        xCoord, yCoord = (0, 0)
        for i in range(self._model.getPlayerBoard().getRows() * 2):
            y1, y2 = (10, 45)
            if(xPix > x1 and xPix < x2):
                    xCoord = i % 10
            for j in range(self._model.getPlayerBoard().getCols()):
                if (yPix > y1 and yPix < y2):
                    yCoord = j % 10
                
                y1 += 35
                y2 += 35

            x1 += 35
            x2 += 35

        return (xCoord, yCoord)
    
    def updateView(self):
        self._view.displayBoards(self._model.getPlayerBoard(), self._model.getAIBoard())
        self._view.getCanvasWidget().bind("<Button-1>", self.clickSpace)

gc = GameController()

gc.updateView()

mainloop()
