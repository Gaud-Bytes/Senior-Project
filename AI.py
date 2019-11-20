import sqlite3 as sql
from Player import Player
from Ship import Ship
from PlayerStrategy import *
from random import randint as rand

class AI(Player):

    def __init__(self, strategy : AIStrategy()):
        super(AI, self).__init__(strategy)
        #Used in parrallel
        self._unattackedSquares = []
        self._leftSquares = []
        self._upSquares = []
        self._rightSquares = []
        self._downSquares = []
        self._successRates = []
        self._gameData = []
        self._sameHighestRate = []
       # self._lastHit = []
       # self._adjacent = []
       # self._currentHitShips = []

    def attack(self, player):
        self.__readGameData(player)
        self.__setUnAttackedSquares(player)
        self.__setSuccessRatesForUnAttackedSquares(player)
        coords = self.__chooseASquare(player)
        self._strategy.attack(player, coords)
        #self.__updateLastHit(player, coords)
        #self.__removeCurrentHitShipsAfterSunk(player)
        self.__updateGameData(player, coords[0], coords[1])

    def placeShip(self, ship):
        self._strategy.placeShip(self, ship)

    def __readGameData(self, player):
        print("Reading Game Data...")
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM SPACE_EVAL''')
        rows = c.fetchall()
        self._gameData = []
        for row in rows:
            self._gameData.append({'left' : row[1], 'up' : row[2], 'right' : row[3], 'down' : row[4], 'success' : row[5], 'total' : row[6]})


        c.close()
        conn.close()
        print("Game Data Read.")

    def __updateGameData(self, player, x, y):

        index = 0
        total = 0
        success = 0
        for i in range(len(self._unattackedSquares)):
            if self._unattackedSquares[i] == player.getBoard().getSpace(x, y):
                index = i
                for data in self._gameData:
                    if self._leftSquares[i] == data['left'] and self._upSquares[i] == data['up'] and self._rightSquares[i] == data['right'] and self._downSquares[i] == data['down']:
                        print(data['success'])
                        success = data['success']
                        total = data['total']
                        break
                break

        print("Updating Game Data...")
        conn = sql.connect('GameData.db')
        c = conn.cursor()

        if(player.getBoard().getSpace(x, y).isAttacked() and player.getBoard().getSpace(x, y).isOccupied()):
            success += 1
            total += 1
        elif(player.getBoard().getSpace(x, y).isAttacked() and not player.getBoard().getSpace(x, y).isOccupied()):
            total += 1

        print(success)
        print(total)
        print(self._leftSquares[index] + self._upSquares[index] + self._rightSquares[index] + self._downSquares[index])

        c.execute('''UPDATE SPACE_EVAL SET 
                        SPACE_EVAL_SUCCESS = ?, SPACE_EVAL_TOTAL = ?
                        WHERE SPACE_EVAL_LEFT = ? and SPACE_EVAL_UP = ? and SPACE_EVAL_RIGHT = ? and SPACE_EVAL_DOWN = ?''', 
                        (success, total, self._leftSquares[index], 
                        self._upSquares[index], self._rightSquares[index], self._downSquares[index]))

       
        #saves and closes connections
        conn.commit()
        c.close()
        conn.close()
        print("Updated Data")

    def __chooseASquare(self, player):
        self._sameHighestRate = []
        rate = 0
        for x in range(len(self._unattackedSquares)):
            if rate < self._successRates[x]:
                self._sameHighestRate = []
                maxi = self._unattackedSquares[x]
                rate = self._successRates[x]
                self._sameHighestRate.append(maxi)

            elif rate == self._successRates[x]:
                self._sameHighestRate.append(self._unattackedSquares[x])

        if len(self._sameHighestRate) == 1:
            print(self._sameHighestRate[0].getCoords())
            return self._sameHighestRate[0].getCoords()

        elif len(self._sameHighestRate) > 1:
            index = rand(0, len(self._sameHighestRate) - 1)
            print(self._sameHighestRate[index].getCoords())
            return self._sameHighestRate[index].getCoords()
            


    def __setUnAttackedSquares(self, player):
        #Have a list of unattacked squares to influence attack choice
        self._unattackedSquares = []
        for x in range(player.getBoard().getRows()):
            for y in range(player.getBoard().getCols()):
                if(not player.getBoard().getSpace(x, y).isAttacked()):
                    self._unattackedSquares.append(player.getBoard().getSpace(x, y))

    def __setSuccessRatesForUnAttackedSquares(self, player):
        if len(self._unattackedSquares) == 0:
            return False

        self._leftSquares = []
        self._upSquares = []
        self._rightSquares = []
        self._downSquares = []

        self._successRates = []

        adjLeft = 'U'
        adjUp = 'U'
        adjRight = 'U'
        adjDown = 'U'

        for space in self._unattackedSquares:
            x = space.getCoords()[0]
            y = space.getCoords()[1]

            #check the status of the left
            leftX = x - 1
            
            if(leftX < 0):
                adjLeft = 'E'
            elif(player.getBoard().getSpace(leftX, y).isAttacked() and player.getBoard().getSpace(leftX, y).isOccupied()):
                adjLeft = 'S'

            elif(player.getBoard().getSpace(leftX, y).isAttacked() and not player.getBoard().getSpace(leftX, y).isOccupied()):
                adjLeft = 'E'
            else:
                adjLeft = 'U'

            self._leftSquares.append(adjLeft)           

            #check the status of the up
            upY = y - 1
            
            if(upY < 0):
                adjUp = 'E'
            elif(player.getBoard().getSpace(x, upY).isAttacked() and player.getBoard().getSpace(x, upY).isOccupied()):
                adjUp = 'S'

            elif(player.getBoard().getSpace(x, upY).isAttacked() and not player.getBoard().getSpace(x, upY).isOccupied()):
                adjUp = 'E'
            else:
                adjUp = 'U'

            self._upSquares.append(adjUp) 

            #check the status of the right
            rightX = x + 1
            if(rightX > 9):
                adjRight = 'E'
            elif(player.getBoard().getSpace(rightX, y).isAttacked() and player.getBoard().getSpace(rightX, y).isOccupied()):
                adjRight = 'S'

            elif(player.getBoard().getSpace(rightX, y).isAttacked() and not player.getBoard().getSpace(rightX, y).isOccupied()):
                adjRight = 'E'
            else:
                adjRight = 'U'

            self._rightSquares.append(adjRight)  

            #check the status of the Down
            downY = y + 1
            if(downY > 9):
                adjDown = 'E'
            elif(player.getBoard().getSpace(x, downY).isAttacked() and player.getBoard().getSpace(x, downY).isOccupied()):
                adjDown = 'S'

            elif(player.getBoard().getSpace(x, downY).isAttacked() and not player.getBoard().getSpace(x, downY).isOccupied()):
                adjDown = 'E'
            else:
                adjDown = 'U'

            self._downSquares.append(adjDown)
        self.__pullSuccessRateFromGameData()

    def __pullSuccessRateFromGameData(self):
        for x in range(0, 100):
            self._successRates.append(0)

        for data in self._gameData:
            for x in range(len(self._unattackedSquares)):
                if(data['left'] == self._leftSquares[x] and data['right'] == self._rightSquares[x] and data['up'] == self._upSquares[x] and data['down'] == self._downSquares[x]):
                        if(not data['total'] == 0):
                            rate = int((data['success'] / data['total']) * 100)
                        else:
                            rate = 0
                        
                        self._successRates[x] = rate

        print(self._successRates)
   