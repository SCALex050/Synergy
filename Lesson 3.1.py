print ("Введите вид питомца")
animal = input()

print ("Введите кличку питомца")
name = input()

print ("Введите возраст")
age = int(input())


if (age%10 == 1) and (age != 11):
    print("Это ", animal, " по кличке ", name, ". Возраст - ", age, " год.", sep = "")

elif (2 <= age%10 <= 4) and not (12 <= age <= 14):
    print ("Это ", animal, " по кличке ", name, ". Возраст - ", age, " года.", sep = "")

else:
    print ("Это ", animal, " по кличке ", name, ". Возраст - ", age, " лет.", sep = "")