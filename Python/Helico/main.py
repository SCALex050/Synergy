from pynput import keyboard
from map import Map
from clouds import Clouds
import time 
import os
import json
from helicopter import Helicopter as Helico

TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 150
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds (MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
tick = 1 


MOVES = {"w": (-1,0), "ц":(-1,0), 
         "d": (0,1), "в": (0,1),
         "s": (1,0), "ы": (1,0), 
         "a": (0,-1), "ф": (0,-1)}

def process_key(key):
    global helico, tick, clouds, field
    if hasattr (key, "char") and key.char: 
        c = key.char.lower()
        if c in MOVES.keys():
            dx,dy = MOVES[c][0], MOVES[c][1]
            helico.move(dx, dy)
        elif c == "f" or c == "а":
            data = {"helicopter": helico.export_data(), 
                    "clouds": clouds.export_data(), 
                    "field": field.export_data(), 
                    "tick":tick}
            folder_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(folder_path, "level.json")
            with open (file_path, "w") as lvl:
                json.dump(data, lvl)
        elif c == "g" or c == "п":
            folder_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(folder_path, "level.json")
            if os.path.exists(file_path):
                with open (file_path, "r") as lvl:
                    data = json.load(lvl)
                    tick = data.get ("tick", 1)
                    helico.import_data(data["helicopter"])
                    field.import_data (data["field"])
                    clouds.import_data (data["clouds"])
            else:
                pass
                
              
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()

os.system("cls" if os.name == "nt" else "clear")

while True:
#    os.system("cls" if os.name == "nt" else "clear") 
    print ("\033[H", end='')
    field.process_helicopter(helico, clouds)
    helico.stats ()
    field.print_map(helico, clouds)
    print ("TICK", tick)
   
    tick +=1 
    time.sleep(TICK_SLEEP)
   
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires(helico)
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()
