from tkinter import *
from Board import Board

class GameView:
    

    def __init__(self, master):
        self._canvas_width, self._canvas_height = (800, 900)
        self._master = master
        self._master.title("BattleBot AI Game")
        self._w = Canvas(self._master, width=self._canvas_width, height=self._canvas_height )
        self._w.pack()

    def getCanvasWidget(self):
        return self._w



    def displayBoards(self, pl, ai):
        x1, y1, x2, y2 = (10, 10, 45, 45)

        self._w.delete(ALL)
        for i in range(ai.getRows()):
            y1 = 10
            y2 = 45
            for j in range(ai.getCols()):
                if(ai.getSpace(i,j).isAttacked() and ai.getSpace(i,j).isOccupied()):
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#B22222")
                elif(ai.getSpace(i,j).isAttacked() and not ai.getSpace(i,j).isOccupied()):
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF")
                else:
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#228B22")

                y1+=35
                y2+=35
            x1+=35
            x2+=35

        for i in range(pl.getRows()):
            y1 = 10
            y2 = 45
            for j in range(pl.getCols()):
                if(pl.getSpace(i,j).isAttacked() and pl.getSpace(i,j).isOccupied()):
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#B22222")
                elif(pl.getSpace(i,j).isAttacked() and not pl.getSpace(i,j).isOccupied()):
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF")
                elif(not pl.getSpace(i,j).isAttacked() and pl.getSpace(i,j).isOccupied()):
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#000000")
                else:
                    self._w.create_rectangle(x1, y1, x2, y2, fill="#00FFFF")
                
                y1+=35
                y2+=35
            x1+=35
            x2+=35


