from Board import Board

class GameModel:
    _playerBoard, _aiBoard = (Board(), Board())

    def __init__(self):
        pass

    def getPlayerBoard(self):
        return self._playerBoard

    def getAIBoard(self):
        return self._aiBoard
