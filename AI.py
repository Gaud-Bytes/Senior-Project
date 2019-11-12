import sqlite3 as sql
from Player import Player
from Ship import Ship
from PlayerStrategy import *

class AI(Player):

    def __init__(self, strategy : AIStrategy()):
        super(AI, self).__init__(strategy)

    def attack(self, player):
        self._strategy.attack(player)

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)

    def readGameData(self):
        pass

    def updateGameData(self, x, y):
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM BOARD WHERE BOARD_X = ? and BOARD_Y = ?''', (x, y))
        space = c.fetchone()

        weight = int(space[2])

        if self._board[x][y].isAttacked() and self._board[x][y].isOccupied():
            weight += 1

        elif self._board[x][y].isAttacked() and not self._board[x][y].isOccupied():
            weight -= 1

        else: 
            c.close()
            conn.close()
            return False

        c.execute('''UPDATE BOARD SET BOARD_WEIGHT = ? WHERE BOARD_X = ? and BOARD_Y = ?''', (weight, x, y))
        conn.commit()
        c.close()
        conn.close()