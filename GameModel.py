from Board import Board

class GameModel:
    
    def __init__(self):
        self._playerBoard, self._aiBoard = (Board("Player"), Board("AI"))
        self._playersTurn = True

    def getPlayerBoard(self):
        return self._playerBoard

    def getAIBoard(self):
        return self._aiBoard

    def getTurn(self):
        return self._playersTurn

    def turnChange(self):
        if(self._playersTurn):
            self._playersTurn = False
        else:
            self._playersTurn = True
