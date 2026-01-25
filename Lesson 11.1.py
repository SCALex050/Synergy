#задание 11.1
lst = []
n = int(input("Введите число n - "))
def fac(n):
    x = 1
    for i in range (1, n+1):
        x *= i
    return (x)

for i in range (fac(n), 0, -1):
    lst.append (fac(i))
print (lst)