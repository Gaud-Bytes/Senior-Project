
class Ship:

    def __init__(self, name, size):
        
        if(isinstance(name, str)):
            self._shipName = name
        else:
            self._shipName = "Patrol Boat"

        if(size < 7 and size > 0):
            self._shipSize = size
        else:
            self._shipSize = 2

        self._sunk = False
        self._placed = False
        self._startSpace, self._endSpace = (None, None)
        self._shipSpaces = []

    def setStart(self, startSpace):

        if(isinstance(startSpace, tuple) and len(startSpace) == 2):
            if(isinstance(startSpace[0], int) and isinstance(startSpace[1], int)):
                self._startSpace = startSpace
                return True

            else:
                return False

        else:
            return False

    def setEnd(self, endSpace):

        if(self._startSpace == None):
            return False
        
        if(isinstance(endSpace, tuple) and len(endSpace) == 2):
            if(isinstance(endSpace[0], int) and isinstance(endSpace[1], int)):
                if(endSpace[0] >= 0 and endSpace[1] >= 0):
                    if(((endSpace[0] == (self._startSpace[0] + self._shipSize - 1)) 
                        or (endSpace[0] == (self._startSpace[0] - (self._shipSize - 1)))) 
                        and (self._startSpace[1] == endSpace[1])):
                        
                        self._endSpace = endSpace
                        self.__setSquareCoords()
                        return True

                    elif(((endSpace[1] == self._startSpace[1] + self._shipSize - 1 ) 
                        or (endSpace[1] == self._startSpace[1] - (self._shipSize - 1))) 
                        and (self._startSpace[0] == endSpace[0])):

                        self._endSpace = endSpace
                        self.__setSquareCoords()
                        return True
                    else:
                        return False

                else:
                    return False

            else:
                return False

        else:
            return False

   
    def getName(self):
        return self._shipName

    def getSize(self):
        return self._shipSize

    def isSunk(self):
        return self._sunk

    def sinkShip(self):
        self._sunk = True

    def resetShip(self):
        self._sunk = False

    def __setSquareCoords(self):
        self._shipSpaces = []
        if((self._endSpace[0] > self._startSpace[0]) or (self._endSpace[1] > self._startSpace[1])):
            for x in range(self._startSpace[0], self._endSpace[0] + 1):
                for y in range(self._startSpace[1], self._endSpace[1] + 1):
                    coords = (x, y)
                    self._shipSpaces.append(coords)

        if((self._endSpace[0] < self._startSpace[0]) or (self._endSpace[1] < self._startSpace[1])):
            for x in range(self._endSpace[0], self._startSpace[0] + 1):
                for y in range(self._endSpace[1], self._startSpace[1] + 1):
                    coords = (x, y)
                    self._shipSpaces.append(coords)

    def getSpaces(self):
        return self._shipSpaces

    def getStart(self):
        return self._startSpace

    def getEnd(self):
        return self._endSpace

    def isPlaced(self):
        return self._placed

    def setPlaced(self):
        self._placed = True
    
    def removeShip(self):
        self._placed = False
        self._sunk = False
        self._shipSpaces = []

