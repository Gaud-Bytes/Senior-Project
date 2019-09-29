from Player import Player
from PlayerStrategy import *

class HumanPlayer(Player):

    def __init__(self):
        super(HumanPlayer, self).__init__(HumanStrategy())

    def attack(self, player, coords):
        self._strategy.attack(player, coords)

    def placeShip(self, startCoords, endCoords):
        self._strategy.placeShip(startCoords, endCoords)
        
