from Board import Board

class GameModel:
    
    def __init__(self):
        self._playerBoard, self._aiBoard = (Board("Player"), Board("AI"))

    def getPlayerBoard(self):
        return self._playerBoard

    def getAIBoard(self):
        return self._aiBoard
