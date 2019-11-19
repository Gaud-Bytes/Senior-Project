from GameModel import GameModel as gm
from GameView import GameView as gv
from tkinter import *

class GameController:

    def __init__(self):
        self._root = Tk()
        self._root.resizable(False, False)
        self._model = gm()
        self._view = gv(self._root, self._model)
        self.__aiInitBoard()
        self.__bindEvents()
        self.__updateView()
        self._root.mainloop()
        

    #PRIVATE functions
    def __clickSpace(self, event):
        
        coords = self.__pixToGridCoord(event.x, event.y)

        if(coords[0] == -1 or coords[1] == -1):
            return False

        if(self._model.isGameOver()):
            print("Game is over")
            return True

        
        if(self._model.isAttackPhase() and self._model.isPlayerOneTurn()):
            self.__attackPhase(coords)
        elif(self._model.isShipPlacementPhase()):
            self.__shipPlacementPhase(coords)
            


        print(coords)
        self.__updateView()
        return True

    def __pixToGridCoord(self, xPix, yPix):
        x1, y1, x2, y2 = (180, 10, 225, 55)
        xCoord, yCoord = (-1, -1)
        yDiff = y2 - y1
        xDiff = x2 - x1
        yMax = yDiff * self._model.getPlayerBoard().getRows() + y2
        xMax = xDiff * self._model.getPlayerBoard().getCols() + x2

        if(xPix > x1 and xPix < xMax) and (yPix > y1 and yPix < yMax ):
            for i in range(self._model.getPlayerBoard().getRows()):
                y1, y2 = (10, 55)
                if(xPix > x1 and xPix < x2):
                        xCoord = i
                for j in range(self._model.getPlayerBoard().getCols()):
                    if (yPix > y1 and yPix < y2):
                        yCoord = j
                    
                    y1 += yDiff
                    y2 += yDiff

                x1 += xDiff
                x2 += xDiff

        return (xCoord, yCoord)

    def __quitgame(self):
        print("Quitting Game")
        self._root.destroy()

    
    def __nextPhase(self):

        self.__checkIfShipsNeedToBeSunk()

        if(not self._model.isGameOver() and self._model.allPlayerShipsSunk(self._model.getAIPlayer()) or self._model.allPlayerShipsSunk(self._model.getPlayer())):
            self._model.endGame()
            self._model.getAIPlayer().endGameUpdate(self._model.getPlayer())

        if(self._model.isShipPlacementPhaseReadyToEnd()):
            print("Advancing to attack Phase")
            self._model.shipPlacementEnd()
            self._model.startAttackPhase()
            self._model.resetShipPhaseEndFlag()
            

        elif(self._model.isAttackPhase() and self._model.isPlayerOneTurn()):
            print("Changing from Player 1s attack to Player 2s")
            self._model.setPlayerTurn(2)
            if(not self._model.isGameOver()):
                self._model.resetAttackPhaseEndFlag()
                self.__aiTurn()

        elif(self._model.isAttackPhase() and self._model.isPlayerTwoTurn()):
            print("Changing from player 2s attack phase to player 1s")
            self._model.setPlayerTurn(1)
            if(not self._model.isGameOver()):
                self._model.resetAttackPhaseEndFlag()
        else:
            print("Failed to advance to next phase")
            return False

        self.__updateView()
        return True

    def __confirmAttack(self):
        if(self._model.isAttackPhase() and self._model.isPlayerOneTurn):
            self._model.getAIBoard().getSpace(
                self._model.getSelectedSpace(0)[0],
                self._model.getSelectedSpace(0)[1]
            ).attack()

            self._model.getAIBoard().getSpace(
                self._model.getSelectedSpace(0)[0],
                self._model.getSelectedSpace(0)[1]
            ).deselect()
            
            self._model.clearAllSelected()
            self._model.setNoSpaceSelected()

            self._model.setAttackPhaseReadyToEnd()

            self.__updateView()

        else:
            print("Can not attack when it is not your turn to attack")
            return False

    def __activeShip(self, index):
        aShip = self._model.getPlayerShips()[index]
        self._model.setActiveShip(aShip, index)
        print("Active Ship: " + aShip.getName())
        self.__updateView()
    
    def __shipPlacementPhase(self, coords):
        if(self._model.getActiveShip() == None):
            print("No Ship Selected")
            return False
        else:
            shipIndex = self._model.getActiveShipIndex()
            print(shipIndex)

            
            self._model.getPlayerBoard().getSpace(coords[0], coords[1]).toggleSelect()

            print(self._model.getSelectedLength())
            if(self._model.getPlayerBoard().getSpace(coords[0], coords[1]).isSelected()):

                self._model.addSelectedSpace(coords)

                if(self._model.getSelectedLength() == 1):
                    self._model.getPlayerShips()[shipIndex].setStart(coords)

                elif(self._model.getSelectedLength() == 2):
                    self._model.getPlayerShips()[shipIndex].setEnd(coords)

                    self._model.getPlayer().placeShip(self._model.getPlayerShips()[shipIndex])
                    self._model.setActiveShip(None, None)

                    self._model.getPlayerBoard().getSpace(
                        self._model.getSelectedSpace(0)[0],
                        self._model.getSelectedSpace(0)[1]
                    ).deselect()

                    self._model.getPlayerBoard().getSpace(
                        self._model.getSelectedSpace(1)[0],
                        self._model.getSelectedSpace(1)[1]
                    ).deselect()

                    self._model.clearAllSelected()
            else:
                self._model.clearAllSelected()

            if(self._model.getPlayer().areAllShipsPlaced()):
                self._model.setShipPlacementPhaseReadyToEnd()
                


    def __attackPhase(self, coords):

        if(not self._model.isAttackPhase()):
            print("Invalid attack phase")
            return False

        elif(self._model.isAttackPhaseReadyToEnd()):
            print("You have attacked this round already")
            return False
        else:

            print(coords)
            if(self._model.getAIBoard().getSpace(coords[0], coords[1]).isAttacked()):
                print("cannot select and already attacked square")
                return False
            
            self._model.getAIBoard().getSpace(coords[0], coords[1]).toggleSelect()

            if(self._model.getAIBoard().getSpace(coords[0], coords[1]).isSelected()):

                if(self._model.getSelectedLength() == 0):
                    self._model.addSelectedSpace(coords)
                    self._model.setSpaceToSelected()
                    print("added single space")

                elif(self._model.getSelectedLength() == 1):
                    
                    self._model.getAIBoard().getSpace(
                        self._model.getSelectedSpace(0)[0],
                        self._model.getSelectedSpace(0)[1]
                    ).deselect()

                    self._model.clearAllSelected()

                    self._model.addSelectedSpace(coords)
                    self._model.setSpaceToSelected()
                    print("changing to new space")

                    return True
            else:
                self._model.clearAllSelected()
                self._model.setNoSpaceSelected()

        
    def __updateView(self):
        self._view.displayBoards()
        self._view.displayButtons()
        self._view.displayAIShipList()

    def __bindEvents(self):

        #button 0-4 ships
        #button 5-7 quit, nextPhase and attack

        #bind events to each ship button 
        for x in range(len(self._model.getPlayerShips())):
            self._view.getButtons()[x].config(command=lambda y=x: self.__activeShip(y))
         
        #bind event to quit button
        self._view.getButtons()[5].config(command=self.__quitgame)

        #bind event to nextPhase Button 
        self._view.getButtons()[6].config(command=self.__nextPhase)

        #bind event to attack button to confirm the attacking of a space
        self._view.getButtons()[7].config(command=self.__confirmAttack)

        #bind click event
        self._view.getCanvasWidget().bind("<Button-1>", self.__clickSpace)

    #Just needed to mock AI placing ships
    def __aiInitBoard(self):
        for ship in self._model.getAIShips():
            self._model.getAIPlayer().placeShip(ship)

    def __aiTurn(self):

        #Logic in attack controlls AIs learning.
        if(self._model.isAttackPhase() and self._model.isPlayerTwoTurn()):
            self._model.getAIPlayer().attack(self._model.getPlayer())
            self._model.setAttackPhaseReadyToEnd()

    def __checkIfShipsNeedToBeSunk(self):

        for ship in self._model.getAIShips():
           if(not ship.isSunk() and self._model.getAIPlayer().allSpacesAttacked(ship)):
                print(ship.getName(), " is Sunk")
                ship.sinkShip()

        for ship in self._model.getPlayerShips():
            if(not ship.isSunk() and self._model.getPlayer().allSpacesAttacked(ship)):
                print(ship.getName(), " is Sunk")
                ship.sinkShip()


        

        


gc = GameController()

