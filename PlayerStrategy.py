from abc import ABC, abstractmethod
from random import randint as rand
class PlayerStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def attack(self, player):
        pass

    @abstractmethod
    def placeShip(self, player, ship):
        pass


class HumanStrategy(PlayerStrategy):

    def __init__(self):
        pass

    def attack(self, player, coords):
        player.getBoard().getSpace(coords[0], coords[1]).attack()

#TODO probably move ship spaces setting to here. Maybe set if a ship is sunk checks in the game itself.
    def placeShip(self, player, ship):
        print(str(ship.getName()))

        print(len(ship.getSpaces()))
        for x in range(len(ship.getSpaces())):
            coords = ship.getSpaces()[x]
            player.getBoard().getSpace(coords[0], coords[1]).occupy()

        

class AIStrategy(PlayerStrategy):

    def __init__(self):
        pass

    def attack(self, player):
        player.getBoard().getSpace(rand(0,10), rand(0,10)).attack()

    def placeShip(self, player, ship):
        start = (rand(0,10), rand(0,10))
        direction = rand(0,2)
        end = [rand(0,10), rand(0,10)]

        end[direction] = start[direction]

        ship.setStart(start)
        ship.setEnd(end)

        for x in range(ship.getSize()):
            coords = ship.getSpaces()[x]
            player.getBoard().getSpace(coords[0], coords[1]).occupy()