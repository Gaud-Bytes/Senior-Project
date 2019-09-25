class Boardspace:

    def __init__(self):
        self._occupied, self._attacked, self._selected = (False, False, False)
        #self._coords = ()

    def occupy(self):
        self._occupied = True

    def attack(self):
        self._attacked = True

   # def setCoords(self, x, y):
        #self._coords = (x, y)
    def toggleSelect(self):
        if not self._selected:
            self._selected = True
        else:
            self._selected = False


    def revertAttack(self):
        self._attacked = False

    def revertOccupy(self):
        self._occupy = False

    def revertAll(self):
        self._occupied, self._attacked, self._selected = (False, False, False)

    def isAttacked(self):
        return self._attacked
    
    def isOccupied(self):
        return self._occupied

    def isSelected(self):
        return self._selected

    #def getCoords(self):
       #return self._coords


    

