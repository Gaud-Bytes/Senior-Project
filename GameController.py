from GameModel import GameModel as gm
from GameView import GameView as gv

class GameController:

    _model = gm()
    _view = gv()    

    def __init__(self, model : gm(), view : gv()):
        self._model = gm()
        self._view = gv()

    