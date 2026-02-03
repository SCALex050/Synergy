#задание 16.1 
command = 0

class  Cassa(object):
    
    def __init__(self, x):
        self.cash = x
    def top_up(self, x):
        cassa_obj.cash += x
    def count_1000(self):
        print (f"В кассе целых тысяч -  { cassa_obj.cash // 1000}.")
    def take_away(self,x):
        if cassa_obj.cash >= x:
            cassa_obj.cash -= x 
        else:
            print ("В кассе недостаточно денег")

cassa_obj = Cassa(0)

while command != "stop":
    command = input ("Введите команду - ").lower()
    if command == "top_up":
        x = int(input("Введите сумму пополнения -"))
        cassa_obj.top_up(x)
    if command == "count":
        cassa_obj.count_1000()
    if command == "take_away":
        x = int(input("Введите сумму изъятия - "))
        cassa_obj.take_away(x)

