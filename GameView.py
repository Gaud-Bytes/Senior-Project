from tkinter import *
from Board import Board

class GameView:
    

    def __init__(self):
        self.canvas_width, self.canvas_height = (800, 900)
        self.master = Tk()
        self.w = Canvas(self.master, width=self.canvas_width, height=self.canvas_height )
        self.w.pack()



    def displayBoards(self, pl : Board(), ai : Board()):
        x1 = 10
        y1 = 10
        x2 = 45
        y2 = 45
        for i in range(ai.getRows()):
            x1 = 10
            x2 = 45
            for j in range(ai.getCols()):
                if(ai.getSpace(i,j).isAttacked() and ai.getSpace(i,j).isOccupied()):
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#B22222")
                elif(ai.getSpace(i,j).isAttacked() and not ai.getSpace(i,j).isOccupied()):
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF")
                else:
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#228B22")
                x1+=35
                x2+=35
            y1+=35
            y2+=35

        for i in range(pl.getRows()):
            x1 = 10
            x2 = 45
            for j in range(pl.getCols()):
                if(pl.getSpace(i,j).isAttacked() and pl.getSpace(i,j).isOccupied()):
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#B22222")
                elif(pl.getSpace(i,j).isAttacked() and not pl.getSpace(i,j).isOccupied()):
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF")
                elif(not pl.getSpace(i,j).isAttacked() and pl.getSpace(i,j).isOccupied()):
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#000000")
                else:
                    self.w.create_rectangle(x1, y1, x2, y2, fill="#00FFFF")
                
                x1+=35
                x2+=35
            y1+=35
            y2+=35
            

        mainloop()


