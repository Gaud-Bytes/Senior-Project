from GameModel import GameModel as gm
from GameView import GameView as gv

class GameController:

    def __init__(self):
        self._model = gm()
        self._view = gv()

    
    def updateView(self):
        self._view.displayBoards(self._model.getPlayerBoard(), self._model.getAIBoard())

gc = GameController()

gc.updateView()


