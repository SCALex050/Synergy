# задание 13.1
import random

def pl(t):
    for i in t:
        print (*i)
    
m = int(input("Введите количество столбцов матрицы - "))
n = int(input("Введите количество строк матрицы - "))
matrix_1 = [[random.randint (-50, 100) for i in range(m)] for i in range(n)]
matrix_2 = [[random.randint (-50, 100) for i in range(m)] for i in range(n)]
matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(m)] for i in range(n)]
print ("Матрица №1:")
pl(matrix_1)
print ("Матрица №2:")
pl (matrix_2)
print ("Сумма двух матриц:")
pl (matrix_3)