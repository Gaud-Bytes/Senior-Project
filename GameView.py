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
        
        #all the ship buttons
        for x in range(len(self._buttons) - 3):
            self._buttons[x].configure(width=10, bg='#ADD8E6', fg="#000000", state=NORMAL)

            if(self._model.getActiveShip() == self._model.getPlayerOneShips()[x]):
                self._buttons[x].configure(width=10, bg='#37FDFC', fg="#000000", state=DISABLED)

            if(self._model.getPlayerOneShips()[x].isPlaced()):
                    self._buttons[x].configure(width=10, bg='#ADD8E6', fg="#000000", state=DISABLED)

            if(self._model.getPlayerOneShips()[x].isSunk()):
                self._buttons[x].configure(width=10, bg='#FF0000', fg="#000000", state=DISABLED)

        #quitButton
        self._buttons[5].configure(width =10, bg='#800000', fg="#FFFFFF")
        
        #Next Phase Button
        
        if(self._model.isShipPlacementPhaseReadyToEnd() or self._model.isAttackPhaseReadyToEnd() or self._model.isGameOver()):
            self._buttons[6].configure(width=10, bg='#00AB66', fg='#000000' , state=NORMAL)
        else:
            self._buttons[6].configure(width=10, bg='#A98307', fg='#FFFFFF', state=DISABLED)

        #Attack Button
        if(self._model.isASpaceSelected()):
            self._buttons[7].configure(width=10, bg='#E0115F', fg='#FFFFFF', state=NORMAL)
        else:
            self._buttons[7].configure(width=10, bg='#800080', fg='#FFFFFF', state=DISABLED)

    def displayAIShipList(self):
        
        #Title Label
        self._shipList[0].configure(width=10, font=("Helvetica", 12))

        #game over label

        if(self._model.allPlayerShipsSunk(self._model.getPlayerOne()) and self._model.isGameOver()):
            self._shipList[1].configure(width=20, font=("Helvetica", 14), fg="#B22222", bg='#FFFFFF', text="Game Over: You Lose")
        elif(self._model.allPlayerShipsSunk(self._model.getPlayerTwo()) and self._model.isGameOver()):
            self._shipList[1].configure(width=20, font=("Helvetica", 14), fg="#228B22", bg='#FFFFFF', text="Game Over: You Win")

        #each ships Label
        for x in range(2, len(self._shipList)):
            self._shipList[x].configure(width=10, font=("Helvetica bold", 12), bg='#FFFFFF')

            if(self._model.getPlayerTwoShips()[x-2].isSunk()):
                self._shipList[x].configure(bg="#B22222", fg='#FFFFFF')

    def displayBoards(self):
        for i in range(len(self._boardSpaces)):
            for j in range(len(self._boardSpaces[i])):
                if self._model.isPlayerOneTurn() and self._model.isAttackPhase():
                    if(self._model.getPlayerTwoBoard().getSpace(i,j).isAttacked() and self._model.getPlayerTwoBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#B22222", width=1)
                    elif(self._model.getPlayerTwoBoard().getSpace(i,j).isAttacked() and not self._model.getPlayerTwoBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#FFFFFF", width=1)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#228B22", width=1)

                    if(self._model.getPlayerTwoBoard().getSpace(i,j).isSelected()):
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#FF6347", width=3)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#000000", width=1)

                else:
                    if(self._model.getPlayerOneBoard().getSpace(i,j).isAttacked() and self._model.getPlayerOneBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#B22222", width=1)
                    elif(self._model.getPlayerOneBoard().getSpace(i,j).isAttacked() and not self._model.getPlayerOneBoard().getSpace(i,j).isOccupied()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#FFFFFF", width=1)
                    elif(self._model.getPlayerOneBoard().getSpace(i, j).isOccupied() and not self._model.getPlayerOneBoard().getSpace(i,j).isAttacked()):
                        self._w.itemconfig(self._boardSpaces[i][j], fill="#AAA9AD", width=1)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j],fill="#17A3F1", width=1)

                    if(self._model.getPlayerOneBoard().getSpace(i,j).isSelected()):
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#FF6347", width=3)
                    else:
                        self._w.itemconfig(self._boardSpaces[i][j], outline="#000000", width=1)

       
    def __createButtons(self):

        buttonX = 150

        for x in range(len(self._model.getPlayerOneShips())):
            buttonX += 100

            if(x == 0):
                shipButtonLabel = self._model.getPlayerOneShips()[x].getName() + "(5)"
            elif(x == 1):
                shipButtonLabel = self._model.getPlayerOneShips()[x].getName() + "(4)"
            elif(x == 2 or x == 3):
                shipButtonLabel = self._model.getPlayerOneShips()[x].getName() + "(3)"
            elif(x == 4):
                shipButtonLabel = self._model.getPlayerOneShips()[x].getName() + "(2)"

            shipButton = Button(self._w, text=shipButtonLabel, anchor=W)
            shipButton_window = self._w.create_window(buttonX, 500, anchor=S, window=shipButton)
            self._buttons.append(shipButton)

        quitB = Button(self._w, text="Quit", anchor=W)
        quitB_window = self._w.create_window(150, 500, anchor=S, window=quitB)

        nextPhase = Button(self._w, text="Next Phase", anchor=W)
        nextPhase_window = self._w.create_window(350, 600, anchor=S, window=nextPhase)

        attackButton = Button(self._w, text="Attack", anchor=W)
        attackButton_window = self._w.create_window(450, 600, anchor=S, window=attackButton)

        self._buttons.append(quitB)
        self._buttons.append(nextPhase)

        self._buttons.append(attackButton)

###PRIVATE functions
    def __createLabels(self):
        labelX = 150

        title = Label(self._w, text="AI Ships:", anchor=W, bg='#AAA9AD' )
        title_window = self._w.create_window(labelX, 550, anchor=S, window=title)

        gameOverLabel = Label(self._w, text="", anchor=W, bg='#000000')
        gameOverLabel_window = self._w.create_window(350, 700, anchor=S, window=gameOverLabel)

        self._shipList.append(title)
        self._shipList.append(gameOverLabel)

        for x in range(len(self._model.getPlayerTwoShips())):
            labelX += 100
            shipLabel = Label(self._w, text=self._model.getPlayerTwoShips()[x].getName(), anchor=W, bg='#AAA9AD' )
            shipLabel.configure(width=10, font=("Helvetica bold", 12))
            shipLabel_window = self._w.create_window(labelX, 550, anchor=S, window=shipLabel)
            self._shipList.append(shipLabel)



    def __createBoard(self):
        x1, y1, x2, y2 = (180, 10, 224, 54)
        yDiff = y2 - y1 + 1
        xDiff = x2 - x1 + 1

        self._boardXmin, self._boardYmin = (x1, y1)
        self._boardXmax, self._boardYmax = (xDiff * self._model.getPlayerOneBoard().getRows() + self._boardXmin, yDiff * self._model.getPlayerOneBoard().getCols() + self._boardYmin )
        
        for x in range(self._model.getPlayerOneBoard().getRows()):
            self._boardSpaces.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        space = NONE
        for i in range(self._model.getPlayerOneBoard().getRows()):
            y1 = 10
            y2 = 54
            yDiff = y2 - y1 + 1
            for j in range(self._model.getPlayerOneBoard().getCols()):
                self._boardSpaces[i][j] = self._w.create_rectangle(x1, y1, x2, y2, fill="#0BB8FF", width=1)
                 

                y1+=yDiff
                y2+=yDiff
            x1+=xDiff
            x2+=xDiff


