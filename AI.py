import sqlite3 as sql
from Player import Player
from Ship import Ship
from PlayerStrategy import *
from random import randint as rand

class AI(Player):

    def __init__(self, strategy : AIStrategy()):
        super(AI, self).__init__(strategy)

    def attack(self, player):
        self.__readGameData(player)
        coords = (rand(0, 9), rand(0, 9))
        self._strategy.attack(player, coords)
        self.__updateGameData(player, coords[0], coords[1])

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)

    def __readGameData(self, player):
        print("Reading Game Data...")
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM BOARD''')
        spaces = c.fetchall()

        for space in spaces:
            x = int(space[0])
            y = int(space[1])
            weight = int(space[2])
            player.getBoard().getSpace(x, y).setWeight(weight)

        c.close()
        conn.close()
        print("Game Data Read.")

    def __updateGameData(self, player, x, y):
        print("Updating Game Data...")
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM BOARD WHERE BOARD_X = ? and BOARD_Y = ?''', (x, y))
        space = c.fetchone()

        weight = int(space[2])

        if player.getBoard().getSpace(x, y).isAttacked() and player.getBoard().getSpace(x, y).isOccupied():
            weight += 1

        elif player.getBoard().getSpace(x, y).isAttacked() and not player.getBoard().getSpace(x, y).isOccupied():
            weight -= 1

        else: 
            print("INVALID OPTION : ", weight)
            c.close()
            conn.close()
            return False

        c.execute('''UPDATE BOARD SET BOARD_WEIGHT = ? WHERE BOARD_X = ? and BOARD_Y = ?''', (weight, x, y))

        #saves and closes connections
        conn.commit()
        c.close()
        conn.close()
        print("Updated Data")