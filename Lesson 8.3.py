# урок 8.3

m = int(input("Введите грузоподъемность лодки - "))
n = int(input("Введите количество рыбаков - "))
w = []
b = 0

for i in range (n):
    w.append (int(input("Введите вес рыбака - ")))
w.sort(reverse = True)

while len(w) > 0:
    if len(w) >= 2:
        if (w[0] + w[-1]) <= m:
            b += 1
            w.pop()
            w.pop(0)
        else:
            b += 1
            w.pop(0)
    else:
        b += 1 
        w.pop(0)
print (f"Количество лодок, чтобы перевести рыбаков - {b}")
