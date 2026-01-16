#урок 6.2
x = int(input())
n = 0
 
for i in range (1, x + 1):
    if x % i == 0:
        n += 1
print(n)    