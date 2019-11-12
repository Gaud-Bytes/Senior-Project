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

    def attack(self, player, coords):
        player.getBoard().getSpace(coords[0], coords[1]).attack()
        
    def placeShip(self, player, ship):

        while(self._isShipConflict(player, ship)):
            start = (rand(0,9), rand(0,9))
            alignment = rand(0, 1)
            direction = rand(0, 1)
            end = [0, 0]

            #print("start: " , start, " align: ", alignment, " Dir: " ,direction)

            end[alignment] = start[alignment]

            #alignment 0 is vertical, alignment 1 is horizental
            if(alignment == 0):
                #direction 0 is up/left and direction 1 is down/right
                if(direction == 0 and start[1] - (ship.getSize() - 1) >= 0):
                    end[1] = start[1] - (ship.getSize() - 1)
                elif(direction == 0 and start[1] + (ship.getSize() - 1) < 10):
                    end[1] = start[1] + (ship.getSize() - 1)
                    
                if(direction == 1 and start[1] - (ship.getSize() - 1) >= 0):
                    end[1] = start[1] - (ship.getSize() - 1)
                elif(direction == 1 and start[1] + (ship.getSize() - 1) < 10):
                    end[1] = start[1] + (ship.getSize() - 1)


            elif(alignment == 1):
                if(direction == 0 and start[0] - (ship.getSize() - 1) >= 0):
                    end[0] = start[0] - (ship.getSize() - 1)
                elif(direction == 0 and start[0] + (ship.getSize() - 1) < 10):
                    end[0] = start[0] + (ship.getSize() - 1)

                if(direction == 1 and start[0] - (ship.getSize() - 1) >= 0):
                    end[0] = start[0] - (ship.getSize() - 1)
                elif(direction == 1 and start[0] + (ship.getSize() - 1) < 10):
                    end[0] = start[0] + (ship.getSize() - 1)

            ship.setStart(start)
           # print("end: ", tuple(end))
            ship.setEnd(tuple(end))

        if(not self._isShipConflict(player, ship)):        
            for x in range(ship.getSize()):
                coords = ship.getSpaces()[x]
                player.getBoard().getSpace(coords[0], coords[1]).occupy()

            ship.setPlaced()
            return True

        else:
            ship.removeShip()
            return False

