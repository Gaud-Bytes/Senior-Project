from Player import Player
from Ship import Ship
from PlayerStrategy import *

class HumanPlayer(Player):

    def __init__(self, strategy : HumanStrategy()):
        super(HumanPlayer, self).__init__(strategy)

    def attack(self, player, coords):
        self._strategy.attack(player, coords)

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)
        
