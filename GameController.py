from GameModel import GameModel as gm
from GameView import GameView as gv
from tkinter import *

class GameController:

    def __init__(self):
        self._root = Tk()
        self._root.resizable(False, False)
        self._model = gm()
        self._view = gv(self._root, self._model)
        self.__bindEvents()
        self.__updateView()

    #PRIVATE functions
    def __clickSpace(self, event):
        
        coords = self.__pixToGridCoord(event.x, event.y)

        if(coords[0] == -1 or coords[1] == -1):
            return False
        
        if(self._model.yourTurn() and not self._model.isShipPlacementPhase()):
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

    def __quitgame(self, event):
        print("Quitting Game")
        self._root.destroy()
        

    def __activeShip(self, index):
        aShip = self._model.getPlayerShips()[index]
        self._model.setActiveShip(aShip, index)

        print("Active Ship: " + aShip.getName())
    
    def __shipPlacementPhase(self, coords):
        if(self._model.getActiveShip() == None):
            print("No Ship Selected")
            return True
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
            

    def __attackPhase(self, coords):
        self._model.getAIBoard().getSpace(coords[0], coords[1]).toggleSelect()
        
    def __updateView(self):
        self._view.displayBoards()
        self._view.displayButtons()
        self._view.displayAIShipList()
    
        #if(not self._model.isShipPlacementPhase):
            #self._model.setActiveShip(None)

        self._root.mainloop()

    def __bindEvents(self):
        
        #button 0-2 quit, confirm, undo.
        #button 3-8 all ship buttons
        
        #bind event to quit button
        self._view.getButtons()[0].bind("<Button>", self.__quitgame)

        #bind events to each ship button
        for x in range(3, len(self._view.getButtons())):
            self._view.getButtons()[x].bind("<Button>", lambda event, y=x-3 : self.__activeShip(y))

        #bind click event
        self._view.getCanvasWidget().bind("<Button-1>", self.__clickSpace)

gc = GameController()

