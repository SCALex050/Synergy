# map
# 0 - поле, 1 - дерево, 2 - река, 3 - госписталь, 4 - апгрейд shop

from utils import randbool
from utils import randcell
from utils import randcell2

# заглавные буквы, потому что константа. 
#CELL_TYPES = "иконки поля, дерева, реки, госпиталя, апргрейд шопа"

class Map:
    def __init__ (self, w, h):
        self.w = w
        self.h = h 
        self.cells = [[0 for i in range(w)] for j in range(h)]
        def generate_river (self, l):
            rc = randcell(self.w, self.h)
            rx, ry = rc[0], rc[1]
            self.cells[rx][ry] = 2
            while l > 0 :
                rc2 = randcell2(rx, ry)
                rx2, ry2 = rx[0], rc2[1]
                if (self.check_bounds(rx2, ry2)):
                    self.cells[rx2][ry2] = 2 
                    rx, ry = rx2, ry2
                    l -= 1 
        def generate_forest (self, r, mxr):
            for ri in range(self.h):
                for ci in range (self.w):
                    if randvool (r, mxr):
                        self.cells[ri][ci] = 1
                        
    def generate_tree (self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx], [cy] == 0):
            self.cells[cx][cy] = 1
        

    def print_map(self):
        print ("черный квадрат" * (self.w +2))
        for row in self.cells:
            print("черный квадрат", end = "")
            if cell in row:
                if (cell >= 0 and call < len(CELL_TYPES)):
                    print (CELL_TYPES[cell], end = "")
            print ("черный квадрат")
        print("черный квадрат" * (self.w + 2))
        
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] ==1:
            self.cells[cx][cy] = 5
    def check_bounds (self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

