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
        #coords = (rand(0, 9), rand(0, 9))
        coords = self.__chooseASquare(player)
        #TODO will be able to get rid of coords parameter when I get the attack decision to be based on the weights rather than random
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

        if player.getBoard().getSpace(x, y).isAttacked() and player.getBoard().getSpace(x, y).isOccupied() and weight < 95:
            weight += 4

        elif player.getBoard().getSpace(x, y).isAttacked() and not player.getBoard().getSpace(x, y).isOccupied() and weight > 1:
            weight -= 1

        else: 
            print("Nothing to be updated")
            c.close()
            conn.close()
            return False

        c.execute('''UPDATE BOARD SET BOARD_WEIGHT = ? WHERE BOARD_X = ? and BOARD_Y = ?''', (weight, x, y))

        #saves and closes connections
        conn.commit()
        c.close()
        conn.close()
        print("Updated Data")

    def __chooseASquare(self, player):

        check = rand(0, 100)
        print("checkVal: ", check)
        tempList = []


        for x in range(player.getBoard().getRows()):
            for y in range(player.getBoard().getCols()):
                tempList.append(player.getBoard().getSpace(x, y))
                #if player.getBoard().getSpace(x, y).getWeight() >= check and not player.getBoard().getSpace(x, y).isAttacked():
                    #return (x, y)
        tempList.sort(key=lambda x : x.getWeight(), reverse=True)

        for space in tempList:
            if space.getWeight() >= check and not space.isAttacked():
                return (space.getCoords()[0], space.getCoords()[1])

        x = rand(0, 9)
        y = rand(0, 9)

        if(not player.getBoard().getSpace(x, y).isAttacked()):
            return (x, y)

        else:
            while(player.getBoard().getSpace(x, y).isAttacked()):
                x = rand(0, 9)
                y = rand(0, 9)

        return (x, y)


