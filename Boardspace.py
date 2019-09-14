class Boardspace:

    occupied, attacked = (False, False)

    def __init__(self):
        pass

    def occupy(self):
        occupied = True

    def attack(self):
        attacked = True

    def revertAttack(self):
        attacked = False

    def revertOccupy(self):
        occupy = False

    def revertAll(self):
        occupied, attacked = (False, False)

    def isAttacked(self):
        return attacked
    
    def isOccupied(self):
        return occupied




