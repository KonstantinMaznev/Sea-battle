from random import randint
class Greet:
    def greeting(self):
        print("Приветствуем вас в игре морской бой")
        print("Формат ввода: x y")
        print("x - номер строки")
        print("y - номер столбца")

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"({self.x}, {self.y})"
class Ship:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Board(Ship):
    def __init__(self, r = 6, c = 6):
        self.cells = []
        self.rowsCount = r
        self.columnsCount = c
        for i in range(r*c):
            self.cells.append(i)

    # def render(self):
    #     rc = self.getRowsCount()
    #     cl = self.getColumnsCount()
    #
    #     # for r in range(rc):
    #     #     row = []
    #     #     for b in range(cl):
    #     #         row.append(b)
    #     #     print("|".join(row))
    #     field = [[' '] * 8 for n in range(7)]
    #     print("  0 | 1 | 2 | 3 | 4 | 5 | 6 |")
    #     for i in range(6):
    #         row_info = " | ".join(field[i])
    #         print(f"{i} {row_info}")

    def getRowsCount(self):
        return self.rowsCount

    def getColumnsCount(self):
        return self.columnsCount

    def getCells(self):
        return self.cells


class Player(Ship):
    def __init__(self):
        super.__init__()
class Computer:
    def
class Win:
    if Player()==0:
        print("Победил Компьютер!")
    else:
        print("Победил Игрок!")
w=Board()
print(w.__init__())
# if __name__ == '__main__':
    # get users
    # swich turns
    # get action