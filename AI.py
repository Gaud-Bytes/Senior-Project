import sqlite3 as sql
from Player import Player
from Ship import Ship
from PlayerStrategy import *
from random import randint as rand

class AI(Player):

    def __init__(self, strategy : AIStrategy()):
        super(AI, self).__init__(strategy)

    def attack(self, player):
        #self.__readGameData()
        coords = (rand(0, 9), rand(0, 9))
        self._strategy.attack(player, coords)
        self.__updateGameData(coords[0], coords[1])

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)

    def __readGameData(self):
        pass

    def __updateGameData(self, x, y):
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM BOARD WHERE BOARD_X = ? and BOARD_Y = ?''', (x, y))
        space = c.fetchone()

        weight = int(space[2])

        if self._board.getSpace(x, y).isAttacked() and self._board.getSpace(x, y).isOccupied():
            weight += 1

        elif self._board.getSpace(x, y).isAttacked() and not self._board.getSpace(x, y).isOccupied():
            weight -= 1

        else: 
            c.close()
            conn.close()
            return False

        c.execute('''UPDATE BOARD SET BOARD_WEIGHT = ? WHERE BOARD_X = ? and BOARD_Y = ?''', (weight, x, y))

        #saves and closes connections
        conn.commit()
        c.close()
        conn.close()