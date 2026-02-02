#задание 14.1 
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rec (x):
    if x == len(my_list):
        print ("Конец списка")
        return
    print (my_list [x])
    rec (x + 1)
rec (0)