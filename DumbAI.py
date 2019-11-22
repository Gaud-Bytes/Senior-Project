from Player import Player
from PlayerStrategy import *
from random import randint

class DumbAI(Player):

    def __init__(self):
        super(DumbAI, self).__init__(AIStrategy())

    def attack(self, player):
        #choose a random square unattacked square
        coords = (rand(0,9), rand(0,9))
        while(player.getBoard().getSpace(coords[0], coords[1]).isAttacked()):
            coords = (rand(0,9), rand(0,9))

        print("DUMB AI ATTACKING : {}".format(coords))
        self._strategy.attack(player, coords)

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)
