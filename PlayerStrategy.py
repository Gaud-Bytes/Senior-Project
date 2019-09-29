from abc import ABC, abstractmethod

class PlayerStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def attack(self, player):
        pass

    @abstractmethod
    def placeShip(self):
        pass


class HumanStrategy(PlayerStrategy):

    def __init__(self):
        pass

    def attack(self, player, coords):
        pass

    def placeShip(self, startCoords, endCoords):
        pass

class AIStrategy(PlayerStrategy):

    def __init__(self):
        pass

    def attack(self, player):
        pass

    def placeShip(self):
        pass