from utils import randcell
import os

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.h = h
        self.w = w 
        self.x = rx
        self.y = ry
        self.mxtank = 1
        self.tank = 0
        self.score = 0 
        self.lives = 20


    def move (self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny
    
    def stats(self):
        print ("🪣  ", self.tank, "/", self.mxtank, sep="", end = " | ")
        print ("🏆", self.score, end= " | ")
        print ("❤️ ", self.lives)

    def game_over (self):
        os.system("cls" if os.name == "nt" else "clear")
        txt = f"XXX  GAME OVER! Your score is - {self.score}  XXX"
        print ("X" * len(txt))
        print(f"XXX {' ' * (len(txt) - 8)} XXX")
        print (txt)
        print(f"XXX {' ' * (len(txt) - 8)} XXX")        
        print ("X" * len(txt))
        exit (0) 

    def export_data (self):
        return {"score": self.score, "lives": self.lives, "x": self.x, "y": self.y, "tank": self.tank, "mxtank": self.mxtank}
    
    def import_data (self, data):
        self.x = data.get("x", 0)
        self.y = data.get ("y", 0)
        self.tank = data.get("tank", 0)
        self.mxtank = data.get("mxtank", 1)
        self.lives = data.get ("lives", 20)
        self.score = data.get ("score", 0)


