from abc import ABC, abstractmethod
from PlayerStrategy import *
from Board import Board
from Ship import Ship

class Player(ABC):

    def __init__(self, strategy):
        if(isinstance(strategy, PlayerStrategy)):
            self._strategy = strategy
        else:
            self._strategy = HumanStrategy()

        self._board = Board()
        self._ships = [Ship("Carrier", 5), Ship("Battleship", 4), Ship("Submarine", 3), Ship("Destroyer", 3), Ship("Patrol Boat", 2)]

    @abstractmethod
    def attack(self, player):
        pass

    @abstractmethod
    def placeShip(self):
        pass

    def getShips(self):
        return self._ships

    def lenShips(self):
        return len(self._ships)

    def getBoard(self):
        return self._board

    def areAllShipsPlaced(self):

        for ship in self._ships:
            if(not ship.isPlaced()):
                return False

        return True

    def areAllShipsSunk(self):
        for ship in self._ships:
            if not ship.isSunk():
                return False

        return True

    def allSpacesAttacked (self, ship):
        for coords in ship.getSpaces():
            if (not self._board.getSpace(coords[0], coords[1]).isAttacked()):
                print("Not Sunk")
                return False

        print(ship.getName(), "why am I turning true by default For AI")

        return True

