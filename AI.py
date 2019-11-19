import sqlite3 as sql
from Player import Player
from Ship import Ship
from PlayerStrategy import *
from random import randint as rand

class AI(Player):

    def __init__(self, strategy : AIStrategy()):
        super(AI, self).__init__(strategy)
        self._lastHit = []
        self._adjacent = []
        self._currentHitShips = []

    def attack(self, player):
        self.__readGameData(player)
        #coords = (rand(0, 9), rand(0, 9))
        coords = self.__chooseASquare(player)
        self._strategy.attack(player, coords)
        self.__updateLastHit(player, coords)
        self.__removeCurrentHitShipsAfterSunk(player)
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
            weight += 3

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

        if(not len(self._lastHit) == 0):

            self.__allAdjacentSet(player)

            checkVal = rand(0, 100)

            print("CheckVal for Adjacent: ", checkVal)
            for space in self._adjacent:
                if space.getWeight() >= checkVal and not space.isAttacked():
                    return (space.getCoords()[0], space.getCoords()[1])


            guess = rand(0, (len(self._adjacent) - 1))
            print("Hitting square: ", (self._adjacent[guess].getCoords()[0], self._adjacent[guess].getCoords()[1]))
            return (self._adjacent[guess].getCoords()[0], self._adjacent[guess].getCoords()[1])

        else:

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

    def __updateLastHit(self, player, coords):
        if(player.getBoard().getSpace(coords[0], coords[1]).isAttacked() and player.getBoard().getSpace(coords[0], coords[1]).isOccupied()):
            self._lastHit.append(player.getBoard().getSpace(coords[0], coords[1]))
            print("ADDED SQUARE: ", (coords[0], coords[1]))

            for hit in self._lastHit:
                print("LastHit: ", hit.getCoords())

            self.__addCurrentHitShips(player, coords)

    def __addCurrentHitShips(self, player, coords):

        for ship in player.getShips():
            if coords in ship.getSpaces() and not ship in self._currentHitShips:
                self._currentHitShips.append(ship)
                print("Hit Ship added: ", ship.getName())
                break

    def __removeCurrentHitShipsAfterSunk(self, player):
        for hit in self._lastHit:
                print("LastHit: ", hit.getCoords())

        #why is second loop out of range or only doing part of lastHit when all other loops transcend the whole list
        for ship in player.getShips():
            if ship.isSunk() and ship in self._currentHitShips:
                print("removing ship: ", ship.getName())
                print("ship Spaces:" ,ship.getSpaces())
                for x in range(0, len(self._lastHit)):
                    print("hitSpace: ", self._lastHit[x].getCoords())
                    if self._lastHit[x].getCoords() in ship.getSpaces():
                        print("removing space: ", self._lastHit[x].getCoords())
                        self._lastHit.remove(self._lastHit[x])


                self._currentHitShips.remove(ship)

    def __allAdjacentSet(self, player):
        self._adjacent = []

        for space in self._lastHit:
            x = space.getCoords()[0]
            y = space.getCoords()[1]

            #left square
            if(x > 0 and not player.getBoard().getSpace((x-1), y).isAttacked()):
                self._adjacent.append(player.getBoard().getSpace((x - 1), y))

            #right square
            if(x < 9 and not player.getBoard().getSpace((x+1), y).isAttacked()):
                self._adjacent.append(player.getBoard().getSpace((x + 1), y))

            #up square
            if(y > 0 and not player.getBoard().getSpace(x, (y-1)).isAttacked()):
                self._adjacent.append(player.getBoard().getSpace(x, (y -1)))

            #down square
            if(y < 9 and not player.getBoard().getSpace(x, (y+1)).isAttacked()):
                self._adjacent.append(player.getBoard().getSpace(x, (y + 1)))

        self._adjacent.sort(key=lambda x : x.getWeight(), reverse=True)

    def endGameUpdate(self, player):

        print("Updating Game Data...")
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM BOARD''')
        spaces = c.fetchall()

        for space in spaces:
            x = int(space[0])
            y = int(space[1])
            weight = int(space[2])
            if(player.getBoard().getSpace(x, y).isAttacked()): continue

            if(player.getBoard().getSpace(x, y).isOccupied() and weight < 98):
                weight += 1
                c.execute('''UPDATE BOARD SET BOARD_WEIGHT = ? WHERE BOARD_X = ? and BOARD_Y = ?''', (weight, x, y))
                print("Updated Data: ", (x, y))
            elif(not player.getBoard().getSpace(x, y).isOccupied() and weight > 1):
                weight -= 1
                c.execute('''UPDATE BOARD SET BOARD_WEIGHT = ? WHERE BOARD_X = ? and BOARD_Y = ?''', (weight, x, y))
                print("Updated Data: ", (x, y))
            else:
                print("Nothing to be updated: ", (x, y))
                continue

        #saves and closes connections
        conn.commit()
        c.close()
        conn.close()


