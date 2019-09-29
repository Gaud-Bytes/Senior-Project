from Player import Player
from HumanPlayer import HumanPlayer as hp
from AI import AI

class GameModel:
    
    def __init__(self):
        self._hPlayer, self._ai = (hp(), AI())
        self._playersTurn = True

    def getPlayerBoard(self):
        return self._hPlayer.getBoard()

    def getAIBoard(self):
        return self._ai.getBoard()

    def playerTurn(self):
        return self._playersTurn

    def turnChange(self):
        if(self._playersTurn):
            self._playersTurn = False
        else:
            self._playersTurn = True
