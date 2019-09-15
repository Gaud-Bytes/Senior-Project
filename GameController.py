from GameModel import GameModel as gm
from GameView import GameView as gv

class GameController:

    _model = gm()
    _view = gv()    

    def __init__(self):
        pass

    
    def updateView(self):
        self._view.displayBoards(self._model.getPlayerBoard(), self._model.getAIBoard())

gc = GameController()

gc.updateView()


