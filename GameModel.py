from Player import Player
from HumanPlayer import HumanPlayer as hp
from AI import AI

class GameModel:
    
    def __init__(self):
        self._hPlayer, self._ai = (hp(), AI())
        self._gameEnd = False
        self._shipPlacementPhase = True
        self._yourTurn = True

    def getPlayerBoard(self):
        return self._hPlayer.getBoard()

    def getAIBoard(self):
        return self._ai.getBoard()

    def yourTurn(self):
        return self._yourTurn

    def turnChange(self):
        if(self._yourTurn):
            self._yourTurn = False
        else:
            self._yourTurn = True

    def shipPlacementEnd(self):
        self._shipPlacementPhase = False

    def endGame(self):
        self._gameEnd = True

    def isShipPlacementPhase(self):
        return self._shipPlacementPhase

    def isGameOver(self):
        return self._gameEnd
