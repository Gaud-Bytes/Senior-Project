from Player import Player
from Ship import Ship
from PlayerStrategy import *

class Model:

    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        self._gameEnd = False

    def getPlayerOne(self):
        return self._player1

    def getPlayerTwo(self):
        return self._player2

    def getPlayerOneBoard(self):
        return self._player1.getBoard()

    def getPlayerTwoBoard(self):
        return self._player2.getBoard()

    def getPlayerOneShips(self):
        return self._player1.getShips()

    def getPlayerTwoShips(self):
        return self._player2.getShips()

    def endGame(self):
        self._gameEnd = True

    def isGameOver(self):
        return self._gameEnd

    def allPlayerShipsSunk(self, player):
        if player.areAllShipsSunk():
            return True

        return False

    def checkIfShipsNeedToBeSunk(self):

        for ship in self.getPlayerTwoShips():
           if(not ship.isSunk() and self.getPlayerTwo().allSpacesAttacked(ship)):
                print(ship.getName(), " is Sunk")
                ship.sinkShip()

        for ship in self.getPlayerOneShips():
            if(not ship.isSunk() and self.getPlayerOne().allSpacesAttacked(ship)):
                print(ship.getName(), " is Sunk")
                ship.sinkShip()