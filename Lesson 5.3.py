#урок 5.3

a = int(input("Введите бюджет Майкла - "))
b = int(input("Введите бюджет Ивана - "))
x = int(input("Введите минимальную сумму инвестиций -"))
 

if a < x < b: print("Иван")

elif b < x < a: print ("Майкл")

elif a < x and b < x and a + b < x: print ("0")

elif a < x and b < x and a + b >= x: print ("1")

else: print ("2")