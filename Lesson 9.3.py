#задание 9.3

lst = list(map(int, input("Введите числа через пробел - ").split()))
num = set()

for i in lst:
    if i in num:
        print (f"{i} Yes")
    else:
        num.add(i)
        print (f"{i} No")