class Boardspace:

    def __init__(self):
        self._occupied, self._attacked, self._selected = (False, False, False)
        self._x , self._y = (0, 0)
        self._weight = 1

    def occupy(self):
        self._occupied = True

    def attack(self):
        self._attacked = True

    def toggleSelect(self):
        if not self._selected:
            self._selected = True
        else:
            self._selected = False


    def revertAttack(self):
        self._attacked = False

    def revertOccupy(self):
        self._occupy = False

    def deselect(self):
        self._selected = False

    def revertAll(self):
        self._occupied, self._attacked, self._selected = (False, False, False)

    def isAttacked(self):
        return self._attacked
    
    def isOccupied(self):
        return self._occupied

    def isSelected(self):
        return self._selected

    def setWeight(self, weight):
        if(isinstance(weight, int) and weight >= 0):
            self._weight = weight
        else:
            return False

    def getWeight(self):
        return self._weight

    def setCoords(self, x, y):
        self._x, self._y = (x, y)

    def getCoords(self):
        return (self._x, self._y)



    

