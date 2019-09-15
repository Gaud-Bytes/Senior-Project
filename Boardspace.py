class Boardspace:

    _occupied, _attacked = (False, False)
    _coords = ()

    def __init__(self):
        pass

    def occupy(self):
        self._occupied = True

    def attack(self):
        self._attacked = True

    def setCoords(self, x, y):
        self._coords = (x, y)

    def revertAttack(self):
        self._attacked = False

    def revertOccupy(self):
        self._occupy = False

    def revertAll(self):
        self._occupied, self._attacked = (False, False)

    def isAttacked(self):
        return self._attacked
    
    def isOccupied(self):
        return self._occupied

    def getCoords(self):
        return self._coords
