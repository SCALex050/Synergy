# урок 8.1 
n = int(input("Введите количество строк - " ))
lst = []

for i in range (n):
    lst.insert(0, int(input("Введите число - ")))
    
print (*lst, sep = " \n")