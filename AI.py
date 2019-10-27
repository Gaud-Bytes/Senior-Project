import sqlite3 as sql
from Player import Player
from Ship import Ship
from PlayerStrategy import *

class AI(Player):

    def __init__(self, strategy : AIStrategy()):
        super(AI, self).__init__(strategy)

    def attack(self, player):
        self._strategy.attack(player)

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)

    def loadData(self):
        pass

    def storeGameData(self):
        pass