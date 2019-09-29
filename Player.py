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

    def getShip(self, index):
        return self._ships[index]

    def getBoard(self):
        return self._board