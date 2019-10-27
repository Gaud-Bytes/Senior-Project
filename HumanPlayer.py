from Player import Player
from Ship import Ship
from PlayerStrategy import *

class HumanPlayer(Player):

    def __init__(self, strategy : HumanStrategy()):
        print("I am a human")
        super(HumanPlayer, self).__init__(strategy)

    def attack(self, player, coords):
        print("Human attack")
        self._strategy.attack(player, coords)

    def placeShip(self, ship):
        print("Human Place Ship")
        self._strategy.placeShip(self, ship)
        
