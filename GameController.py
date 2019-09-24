from GameModel import GameModel as gm
from GameView import GameView as gv
from tkinter import *

class GameController:

    def __init__(self):
        self._root = Tk()
        self._model = gm()
        self._view = gv(self._root)

    
    def clickSpace(self, event):
        print(event.x)
        self.updateView()
    
    def updateView(self):
        self._view.displayBoards(self._model.getPlayerBoard(), self._model.getAIBoard())
        self._view.getCanvasWidget().bind("<Button-1>", self.clickSpace)

gc = GameController()

gc.updateView()

mainloop()
