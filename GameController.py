from GameModel import GameModel as gm
from GameView import GameView as gv
from tkinter import *

class GameController:

    def __init__(self):
        self._root = Tk()
        #self._root.resizable(False, False)
        self._model = gm()
        self._view = gv(self._root)
        self.updateView()

    
    def clickSpace(self, event):
        
        coords = self.pixToGridCoord(event.x, event.y)

        if(coords[0] == -1 or coords[1] == -1):
            return False
        
        if(self._model.yourTurn() and not self._model.isShipPlacementPhase()):
            self.attackPhase(coords)
        elif(self._model.isShipPlacementPhase()):
            self.shipPlacementPhase(coords)


        print(coords)
        self.updateView()
        return True

    def pixToGridCoord(self, xPix, yPix):
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

    def quitgame(self, event):
        print("Quitting Game")
        self._root.destroy()
        

    def activeShip(self, index):
        aShip = self._model.getPlayerShips()[index]
        self._model.setActiveShip(aShip, index)

        print("Active Ship: " + aShip.getName())

    def shipPlacementPhase(self, coords):
        selectedSpaces = []
        shipIndex = self._model.getActiveShipIndex()

        self._model.getPlayerBoard().getSpace(coords[0], coords[1]).toggleSelect()

        selectedSpaces.append(coords)

        if(len(selectedSpaces) == 2):
            self._model.getPlayerShips()[shipIndex].setStart(coords[0])
            self._model.getPlayerShips()[shipIndex].setEnd(coords[1])
            self._model.getPlayer().placeShip(self._model.getPlayer(), self._model.getPlayerShips()[shipIndex], selectedSpaces[0], selectedSpaces[1])
            

    def attackPhase(self, coords):
        self._model.getAIBoard().getSpace(coords[0], coords[1]).toggleSelect()
        
    def updateView(self):
        self._view.displayBoards(self._model)
        self._view.displayButtons(self._model.getPlayerShips())
        self._view.displayAIShipList(self._model.getAIShips())
    
        self._view.getButtons()[0].bind("<Button>", self.quitgame)

        self._view.getButtons()[3].bind("<Button>", lambda event, x=3-3 : self.activeShip(x))
        self._view.getButtons()[4].bind("<Button>", lambda event, x=4-3 : self.activeShip(x))
        self._view.getButtons()[5].bind("<Button>", lambda event, x=5-3 : self.activeShip(x))
        self._view.getButtons()[6].bind("<Button>", lambda event, x=6-3 : self.activeShip(x))
        self._view.getButtons()[7].bind("<Button>", lambda event, x=7-3 : self.activeShip(x))

        if(not self._model.isShipPlacementPhase):
            self._model.setActiveShip(None)

        self._view.getCanvasWidget().bind("<Button-1>", self.clickSpace)
        self._root.deiconify()
        self._root.mainloop()

gc = GameController()

