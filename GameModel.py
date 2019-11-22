from Player import Player
from Model import Model
from Ship import Ship
from HumanPlayer import HumanPlayer as hp
from AI import AI
from PlayerStrategy import *

class GameModel(Model):
    
    def __init__(self):
        super(GameModel, self).__init__(hp(), AI())
        self._shipPlacementPhase = True
        self._attackPhase = False
        self._firstPlayerTurn = True
        self._secondPlayerTurn = False
        self._shipPlacementPhaseReadyToEnd = False
        self._attackPhaseReadyToEnd = False
        self._spaceSelected = False
        self._activeShip = None
        self._activeShipIndex = None
        self._selectedSpaces = []

    def setPlayerTurn(self, num):
        if(isinstance(num, int) and num == 1):
            self._firstPlayerTurn = True
            self._secondPlayerTurn = False

        else:
            self._firstPlayerTurn = False
            self._secondPlayerTurn = True

    def isPlayerOneTurn(self):
        return self._firstPlayerTurn

    def isPlayerTwoTurn(self):
        return self._secondPlayerTurn


    def shipPlacementEnd(self):
        self._shipPlacementPhase = False

    def endGame(self):
        self._gameEnd = True

    def isShipPlacementPhase(self):
        return self._shipPlacementPhase

    def isAttackPhase(self):
        return self._attackPhase

    def setActiveShip(self, ship, index):
        self._activeShip = ship
        self._activeShipIndex = index

    def getActiveShip(self):
        return self._activeShip

    def getActiveShipIndex(self):
        return self._activeShipIndex

    def getSelectedLength(self):
        return len(self._selectedSpaces)

    def addSelectedSpace(self, space):
            self._selectedSpaces.append(space)

    def getSelectedSpace(self, index):
        return self._selectedSpaces[index]

    def clearAllSelected(self):
        self._selectedSpaces = []
        
    def isShipPlacementPhaseReadyToEnd(self):
        return self._shipPlacementPhaseReadyToEnd

    def isAttackPhaseReadyToEnd(self):
        return self._attackPhaseReadyToEnd

    def setShipPlacementPhaseReadyToEnd(self):
        self._shipPlacementPhaseReadyToEnd = True

    def resetShipPhaseEndFlag(self):
        self._shipPlacementPhaseReadyToEnd = False

    def setAttackPhaseReadyToEnd(self):
        self._attackPhaseReadyToEnd = True

    def resetAttackPhaseEndFlag(self):
        self._attackPhaseReadyToEnd = False

    def startAttackPhase(self):
        if(self._shipPlacementPhase):
            self._attackPhase = False
        else:
            self._attackPhase = True

    def startShipPlacementPhase(self):
        if(self._attackPhase):
            self._shipPlacementPhase = False
        else:
            self._shipPlacementPhase = True

    def setSpaceToSelected(self):
        self._spaceSelected = True

    def setNoSpaceSelected(self):
        self._spaceSelected = False

    def isASpaceSelected(self):
        return self._spaceSelected


