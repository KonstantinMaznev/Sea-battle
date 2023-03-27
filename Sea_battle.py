class Greet:
    def greeting(self):
        print("Приветствуем вас в игре морской бой")
class Board:
    def __init__(self, r = 6, c = 6):
        self.cells = []
        self.rowsCount = r
        self.columnsCount = c
        for i in range(r*c):
            self.cells.append(i)

    def getRowsCount(self):
        return self.rowsCount

    def getColumnsCount(self):
        return self.columnsCount

    def getCells(self):
        return self.cells
class Ship:
    def __init__(self,x,y):
        self.x=x
        self.y=y