import tkinter as tk 
import sys
import random


class GameApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.frame=tk.Frame(self.parent)
        self.frame.grid(row=0, column=0, sticky="NSEW")
        tk.Grid.rowconfigure(self.frame, 0, weight=1)
        tk.Grid.columnconfigure(self.frame, 0, weight=1)

        self.tiles = []
        self.createTilesArray()

        for x in range(4):
            tk.Grid.columnconfigure(self.frame, x, weight=1)
            tk.Grid.rowconfigure(self.frame, x, weight=1)

        self.addRandomTiles()
        self.addRandomTiles()


    def createTilesArray(self):
        for x in range(4):
            self.tiles.append([])
            for y in range(4):
                s = tk.StringVar()
                label = tk.Button(self.frame,textvariable=s, height = 5, width = 10)
                s.set(str(""))

                label.grid(column=y, row=x)
                self.tiles[x].append(s)

    def addRandomTiles(self):
        nonZero= []
        for i in range(4):
            for j in range(4):
                if self.tiles[i][j].get() == "":
                    nonZero.append(self.tiles[i][j])

        if len(nonZero) == 0:
            return

        randomSlot = random.randint(0,len(nonZero) - 1)
        nonZero[randomSlot].set(random.randint(1,2) * 2)

    def collapseAdjacentCells(self, cellList):
        anyChanges = False
        for i in range(4):
            #Move current cell over
            if cellList[i].get() == "":
                k = i + 1
                while k < 4:
                    if cellList[k].get() != "":
                        cellList[i].set(cellList[k].get())
                        cellList[k].set("")
                        anyChanges = True
                        break
                    else:
                        k += 1

            #collapse cells together
            k = i + 1
            while k < 4:
                if cellList[k].get() == "":
                    k += 1
                    continue

                if cellList[i].get() == cellList[k].get():
                    value = int(cellList[i].get())
                    cellList[i].set(str(value * 2))
                    cellList[k].set("")
                    anyChanges = True
                break

        return anyChanges



    def leftPressed(self, event):
        anyChanges = False
        for i in range(4):
            cells = []
            for j in range(4):
                cells.append(self.tiles[i][j])

            if self.collapseAdjacentCells(cells):
                anyChanges = True
        
        if anyChanges:
            self.addRandomTiles()

    def rightPressed(self, event):
        anyChanges = False
        for i in range(4):
            cells = []
            for j in range(4):
                cells.append(self.tiles[i][3 - j])

            if self.collapseAdjacentCells(cells):
                anyChanges = True

        if anyChanges:
            self.addRandomTiles()

    def downPressed(self, event):
        anyChanges = False
        for i in range(4):
            cells = []
            for j in range(4):
                cells.append(self.tiles[3 - j][i])

            if self.collapseAdjacentCells(cells):
                anyChanges = True
        
        if anyChanges:
            self.addRandomTiles()


    def upPressed(self, event):
        anyChanges = False
        for i in range(4):
            cells = []
            for j in range(4):
                cells.append(self.tiles[j][i])

            if self.collapseAdjacentCells(cells):
                anyChanges = True

        if anyChanges:
            self.addRandomTiles()



def escPressed(event):
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)

    root.title("2048 Game")
    root.minsize(width=300, height=200)
    root.maxsize(width=300, height=200)

    game = GameApp(root)
    root.bind("<Escape>", escPressed)
    root.bind("<Left>", game.leftPressed)
    root.bind("<Right>", game.rightPressed)
    root.bind("<Down>", game.downPressed)
    root.bind("<Up>", game.upPressed)

    root.mainloop()