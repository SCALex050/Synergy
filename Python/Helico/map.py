#🟩🌳🟦🏥🏠🔥🚁⛈️🌨️❤️🏆⬛🪣
from utils import randbool
from utils import randcell
from utils import randcell2
import os

CELL_TYPES = "🟩", "🌳", "🟦", "🏥", "🏠", "🔥" 
#награда за потушенное дерево
TREE_BONUS = 150
#штраф за сгоревшее дерево
TREE_BURNED = 10
UPGRADE_COST = 1000
LIFE_COST = 1500

class Map:
    def __init__ (self, w, h):
        self.w = w
        self.h = h 
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_upgrade_shop()
        self.generate_hospital()
        self.generate_river(10)
        self.generate_river(10)
        self.generate_forest(45,100)

    def check_bounds (self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True  
    
    def print_map(self, helico, clouds):
        print ("⬛" * (self.w + 2))
        for ri in range(self.h):
            print("⬛", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells [ri][ci] == 1):
                    print ("🌨️ ", end="")
                elif (clouds.cells [ri][ci] == 2):
                    print ("⛈️ ", end="")  
                elif (helico.x == ri and helico.y == ci):
                    print ("🚁", end="")
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print (CELL_TYPES[cell], end="")
            print ("⬛")
        print("⬛" * (self.w + 2))

    def generate_river (self, l):
            rc = randcell(self.w, self.h)
            rx, ry = rc[0], rc[1]
            if self.cells[rx][ry] not in [3, 4]:
                self.cells[rx][ry] = 2
                count = 0
                while l > 0 and count < 100:
                    count += 1
                    rc2 = randcell2(rx, ry)
                    rx2, ry2 = rc2[0], rc2[1]
                    if (self.check_bounds(rx2, ry2)):
                        if self.cells[rx2][ry2] not in [2,3,4]:
                            self.cells[rx2][ry2] = 2 
                            rx, ry = rx2, ry2
                            l -= 1
                            count = 0
                        

    def generate_forest (self, r, mxr):
            for ri in range(self.h):
                for ci in range (self.w):
                    if self.cells[ri][ci] == 0:
                        if randbool (r, mxr):
                            self.cells[ri][ci] = 1
    
    def generate_tree (self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1
    
    def generate_upgrade_shop(self):
        while True:
            c = randcell(self.w, self.h)
            cx, cy = c[0], c[1]
            if self.cells[cx][cy] == 0:
                self.cells[cx][cy] = 4
                break
            
        
    def generate_hospital(self):
        while True:
            c = randcell(self.w, self.h)
            cx, cy = c[0], c[1]
            if self.cells[cx][cy] == 0:
                self.cells[cx][cy] = 3
                break
        
        
                      
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] ==1:
            self.cells[cx][cy] = 5

    def update_fires(self, helico):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    if helico.score >= TREE_BURNED:
                        helico.score -= TREE_BURNED
                    else:
                        helico.score = 0
            for i in range (2):
                self.add_fire()
    
    def process_helicopter(self, helico,clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank +=1
            helico.score -= UPGRADE_COST
        if (c == 3 and helico.score >= LIFE_COST):
            helico.lives +=10
            helico.score -= LIFE_COST
        if d == 2 :
            helico.lives -= 1
            if (helico.lives == 0):
                helico.game_over ()
             
    def export_data(self):
        return {"cells": self.cells}
    
    def import_data (self, data):
        self.cells = data.get("cells") or [[0 for i in range(self.w)] for j in range(self.h)]

    


