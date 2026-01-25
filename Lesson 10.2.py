#задание 10.2

a = int(input ("Введите первое число - "))
b = int(input ("Введите последнее число - "))
c = {}

if a < b: step = 1
else: step = -1
    
for i in range (a, b+step, step):
    c.update ({ i: i**i} )

