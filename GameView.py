from tkinter import *
from GameModel import GameModel as gm
from Board import Board

class GameView:
    

    def __init__(self, master, model):

        if(not isinstance(model, gm) or not isinstance(master, Tk)):
            return

        self._model = model
        self._canvas_width, self._canvas_height = (800, 900)
        self._boardXmin, self._boardyMin, self._boardXmax, self._boardYmax =  (0, 0, 0, 0)
        self._master = master
        self._master.title("BattleBot AI Game")
        self._w = Canvas(self._master, width=self._canvas_width, height=self._canvas_height, bg='#000000' )
        self._w.pack()
        self._buttons = []
        self._shipList = []
        self._boardSpaces = []

        self.__createButtons()
        self.__createLabels()
        self.__createBoard()

#PUBLIC FUNCTIONS
    def getCanvasWidget(self):
        return self._w

    def getButtons(self):
        return self._buttons

    def displayButtons(self):

        #quitButton
        self._buttons[0].configure(width =10, bg='#800000', fg="#FFFFFF")
        
        #confirmButton
        self._buttons[1].configure(width=10, bg='#D4AF37')

        #undoButton
        self._buttons[2].configure(width=10, bg='#E0115F')

        #all the ship buttons
        for x in range(3, len(self._buttons)):
            self._buttons[x].configure(width=10, bg='#ADD8E6', fg="#000000")
                

    def displayAIShipList(self):
        
        #Title Label
        self._shipList[0].configure(width=10, font=("Helvetica", 12))

        #each ships Label
        for x in range(1, len(self._shipList)):
            self._shipList[x].configure(width=10, font=("Helvetica bold", 12))

    def displayBoards(self):
        for i in range(len(self._boardSpaces)):
            for j in range(len(self._boardSpaces[i])):
                if self._model.yourTurn() and not self._model.isShipPlacementPhase():
                    if(self._model.getAIBoard().getSpace(i,j).isAttacked() and self._model.getAIBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#B22222", width=1)
                    elif(self._model.getAIBoard().getSpace(i,j).isAttacked() and not self._model.getAIBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#FFFFFF", width=1)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#228B22", width=1)

                    if(self._model.getAIBoard().getSpace(i,j).isSelected()):
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#FF6347", width=3)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#000000", width=1)

                else:
                    if(self._model.getPlayerBoard().getSpace(i,j).isAttacked() and self._model.getPlayerBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#B22222", width=1)
                    elif(self._model.getPlayerBoard().getSpace(i,j).isAttacked() and not self._model.getPlayerBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#FFFFFF", width=1)
                    elif(self._model.getPlayerBoard().getSpace(i, j).isOccupied() and not self._model.getPlayerBoard.getSpace(i,j).isAttacked()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#AAA9AD", width=1)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j],fill="#0BB8FF", width=1)

                    if(self._model.getPlayerBoard().getSpace(i,j).isSelected()):
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#FF6347", width=3)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#000000", width=1)

       
    def __createButtons(self):

        buttonX = 150

        quitB = Button(self._w, text="Quit", anchor=W)
        quitB_window = self._w.create_window(buttonX, 500, anchor=S, window=quitB)

        confirm = Button(self._w, text="Confrim", anchor=W)
        confirm_window = self._w.create_window(350, 600, anchor=S, window=confirm)

        undo = Button(self._w, text="Undo", anchor=W)
        undo_window = self._w.create_window(450, 600, anchor=S, window=undo)

        self._buttons.append(quitB)
        self._buttons.append(confirm)
        self._buttons.append(undo)

        for x in range(len(self._model.getPlayerShips())):
            buttonX += 100
            shipButton = Button(self._w, text=self._model.getPlayerShips()[x].getName(), anchor=W)
            shipButton_window = self._w.create_window(buttonX, 500, anchor=S, window=shipButton)
            self._buttons.append(shipButton)

###PRIVATE functions
    def __createLabels(self):
        labelX = 150

        title = Label(self._w, text="AI Ships:", anchor=W, bg='#AAA9AD' )
        title_window = self._w.create_window(labelX, 550, anchor=S, window=title)

        self._shipList.append(title)

        for x in range(len(self._model.getAIShips())):
            labelX += 100
            shipLabel = Label(self._w, text=self._model.getAIShips()[x].getName(), anchor=W, bg='#AAA9AD' )
            shipLabel.configure(width=10, font=("Helvetica bold", 12))
            shipLabel_window = self._w.create_window(labelX, 550, anchor=S, window=shipLabel)
            self._shipList.append(shipLabel)

    def __createBoard(self):
        x1, y1, x2, y2 = (180, 10, 224, 54)
        yDiff = y2 - y1 + 1
        xDiff = x2 - x1 + 1

        self._boardXmin, self._boardYmin = (x1, y1)
        self._boardXmax, self._boardYmax = (xDiff * self._model.getPlayerBoard().getRows() + self._boardXmin, yDiff * self._model.getPlayerBoard().getCols() + self._boardYmin )
        
        for x in range(self._model.getPlayerBoard().getRows()):
            self._boardSpaces.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        space = NONE
        for i in range(self._model.getPlayerBoard().getRows()):
            y1 = 10
            y2 = 54
            yDiff = y2 - y1 + 1
            for j in range(self._model.getPlayerBoard().getCols()):
                self._boardSpaces[i][j] = self._w.create_rectangle(x1, y1, x2, y2, fill="#0BB8FF", width=1)
                 

                y1+=yDiff
                y2+=yDiff
            x1+=xDiff
            x2+=xDiff


