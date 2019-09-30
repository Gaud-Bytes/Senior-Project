from tkinter import *
from GameModel import GameModel as gm
from Board import Board

class GameView:
    

    def __init__(self, master):
        self._canvas_width, self._canvas_height = (800, 900)
        self._boardXmin, self._boardyMin, self._boardXmax, self._boardYmax =  (0, 0, 0, 0)
        self._master = master
        self._master.title("BattleBot AI Game")
        self._w = Canvas(self._master, width=self._canvas_width, height=self._canvas_height )
        self._w.pack()

    def getCanvasWidget(self):
        return self._w


    def displayButtons(self, pl):
        button1 = Button(self._w, text="Quit", anchor=W)
        button1.configure(width =10, bg='#800000', fg="#FFFFFF")
        button_window = self._w.create_window(150, 500, anchor=S, window = button1)

    def displayAIShipList(self, ai):
        pass

    def displayPlayerShipList(self, pl):
        pass

    def displayBoards(self, model):

        if(not isinstance(model, gm)):
            return False

        x1, y1, x2, y2 = (180, 10, 224, 54)
        yDiff = y2 - y1 + 1
        xDiff = x2 - x1 + 1

        self._boardXmin, self._boardYmin = (x1, y1)
        self._boardXmax, self._boardYmax = (xDiff * model.getPlayerBoard().getRows() + self._boardXmin, yDiff * model.getPlayerBoard().getCols() + self._boardYmin )
        
        space = NONE

        self._w.delete(ALL)

        if model.yourTurn() and not model.isShipPlacementPhase():
            for i in range(model.getAIBoard().getRows()):
                y1 = 10
                y2 = 54
                yDiff = y2 - y1 + 1
                for j in range(model.getAIBoard().getCols()):
                    if(model.getAIBoard().getSpace(i,j).isAttacked() and model.getAIBoard().getSpace(i,j).isOccupied()):
                        space = self._w.create_rectangle(x1, y1, x2, y2, fill="#B22222", width=1)
                    elif(model.getAIBoard().getSpace(i,j).isAttacked() and not model.getAIBoard().getSpace(i,j).isOccupied()):
                        space =self._w.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", width=1)
                    else:
                        space = self._w.create_rectangle(x1, y1, x2, y2, fill="#228B22", width=1)

                    if(model.getAIBoard().getSpace(i,j).isSelected()):
                        self._w.itemconfig(space, outline="#FF6347", width=3)

                    y1+=yDiff
                    y2+=yDiff
                x1+=xDiff
                x2+=xDiff
        else:
            for i in range(model.getPlayerBoard().getRows()):
                y1 = 10
                y2 = 54
                yDiff = y2 - y1 + 1
                for j in range(model.getPlayerBoard().getCols()):
                    if(model.getPlayerBoard().getSpace(i,j).isAttacked() and model.getPlayerBoard().getSpace(i,j).isOccupied()):
                        space = self._w.create_rectangle(x1, y1, x2, y2, fill="#B22222", width=1)
                    elif(model.getPlayerBoard().getSpace(i,j).isAttacked() and not model.getPlayerBoard().getSpace(i,j).isOccupied()):
                       space = self._w.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", width=1)
                    elif(not model.getPlayerBoard().getSpace(i,j).isAttacked() and model.getPlayerBoard().getSpace(i,j).isOccupied()):
                        space = self._w.create_rectangle(x1, y1, x2, y2, fill="#000000", width=1)
                    else:
                       space = self._w.create_rectangle(x1, y1, x2, y2, fill="#00FFFF", width=1)

                    if(model.getPlayerBoard().getSpace(i,j).isSelected()):
                        self._w.itemconfig(space, outline="red", width=5)
                    
                    y1+=yDiff
                    y2+=yDiff
                x1+=xDiff
                x2+=xDiff


