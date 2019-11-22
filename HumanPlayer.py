from Player import Player
from Ship import Ship
from PlayerStrategy import *

class HumanPlayer(Player):

    def __init__(self):
        super(HumanPlayer, self).__init__(HumanStrategy())

    def attack(self, player, coords):
        self._strategy.attack(player, coords)

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)
        
