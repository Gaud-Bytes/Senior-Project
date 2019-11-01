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

    def _isShipConflict(self, player, ship):

        if(len(ship.getSpaces()) == 0):
            return True

        for pShip in player.getShips():
            if(not (pShip == ship)):
                for x in range(len(pShip.getSpaces())):
                    for y in range(len(ship.getSpaces())):
                        if(pShip.getSpaces()[x] == ship.getSpaces()[y]):
                            return True
        return False


class HumanStrategy(PlayerStrategy):

    def __init__(self):
        pass

    def attack(self, player, coords):
        player.getBoard().getSpace(coords[0], coords[1]).attack()

    def placeShip(self, player, ship):
        # should place ship if no overlapping squares. if there is overlap undo the placement
        if(not self._isShipConflict(player, ship)):
            for x in range(len(ship.getSpaces())):
                coords = ship.getSpaces()[x]
                player.getBoard().getSpace(coords[0], coords[1]).occupy()

            ship.setPlaced()
            return True

        else:
            ship.removeShip()
            return False

        

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