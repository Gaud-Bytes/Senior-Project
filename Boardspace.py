class Boardspace:

    occupied = False
    attacked = False

    def occupy(self):
        occupied = True

    def attack(self):
        attacked = True

    def revertAttack(self):
        attacked = False

    def revertOccupy(self):
        occupy = False

    def revertAll(self):
        attacked = False
        occupied = False

    def getAtkState(self):
        return attacked
    
    def getOccupiedState(self):
        return occupied




