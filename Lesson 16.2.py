# задание 16.2
command = 0
class Turtle(object):
    def __init__ (self, x, y, s):
        self.pos_x = x
        self.pos_y = y
        self.move_s = s

    def go_up(self):
        self.pos_y += self.move_s

    def go_down(self):
        self.pos_y -= self.move_s

    def go_left(self):
        self.pos_x -= self.move_s

    def go_right(self):
        self.pos_x += self.move_s

    def evolve(self):
        self.move_s += 1

    def degrade(self):
        if self.move_s >1:
            self.move_s -= 1
        else:
            print ("Error")

    def count_moves (self, x2, y2):
        mx = ((abs(x2 - self.pos_x)) + self.move_s - 1) // self.move_s
        my = ((abs(y2 - self.pos_y)) + self.move_s - 1) // self.move_s
        print (f"Чтобы дойти до новых координат потребуется шагов - {mx + my}.")

 

turt = Turtle(1, 1, 1)

 

while command != "stop":
    command = input("Введите команду:").lower()

    if command == "go_up":
        turt.go_up()

    elif command == "go_down":
        turt.go_down()

    elif command == "go_left":
        turt.go_left()

    elif command == "go_right":
        turt.go_right()

    elif command == "evolve":
        turt.evolve()

    elif command == "degrade":
        turt.degrade()

    elif command == "count_moves":
        x2 = int(input("Введите x2: "))
        y2 = int(input("Введите y2: "))
        turt.count_moves(x2, y2)

    elif command == "check":
        print(f"Координаты x: {turt.pos_x}, координаты y: {turt.pos_y}, шаг: {turt.move_s}")