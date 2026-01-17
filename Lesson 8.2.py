# урок 8.2 

n = int(input("Введите количество чисел - "))
str = list(map(int, input ("Введите числа через пробел - ").split()))
x  = str.pop(n-1)
str.insert (0, x)

print (str)
