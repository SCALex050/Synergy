# задание 11.2
import collections
pets = {}   
command = 0

def create ():
    if not pets:
        pet_id = 1
    else:
        last = collections.deque(pets, maxlen=1)[0]
        pet_id = last + 1
    pets[pet_id] = {input("Введите имя питомца - ") : {
    "Вид питомца": input("Введите вид питомца - "),
    "Возраст питомца": int(input("Введите возраст питомца - ")),
    "Имя владельца": input("Введите имя владельца - ")}
}

def read (pet_id = None):
    if pet_id is None:
        pet_id = get_id()
    if pet_id: 
        pet_name = next(iter(pets[pet_id]))
        print(f"Это {pets[pet_id][pet_name]['Вид питомца']} по кличке {pet_name}."
        f" Возраст питомца - {get_suffix(pets[pet_id][pet_name]['Возраст питомца'])}."
        f" Имя владельца - {pets[pet_id][pet_name]['Имя владельца']}.")

def update ():
    pet_id = get_id()
    if pet_id: 
        pets[pet_id] = {input("Введите имя питомца - ") : {
        "Вид питомца": input("Введите вид питомца - "),
        "Возраст питомца": int(input("Введите возраст питомца - ")),
        "Имя владельца": input("Введите имя владельца - ")}
    }
def delete ():
    pet_id = get_id()
    if pet_id:
        del pets[pet_id]

def get_id():
    pet_id = int(input("Введите ID питомца - "))
    if pet_id not in pets:
        print ("Нет такого ID")
        return False
    return pet_id

def get_suffix(age):
    if (age %10 == 1) and (age != 11):
        return (f"{age} год")
    elif (2 <= age %10 <= 4) and not (12 <= age <= 14):
        return (f"{age} года")
    else:
        return (f"{age} лет")
        
def pet_list():
    if not pets:
        print ("Список пуст")
    else:
        for pet_id in pets:
            read (pet_id)
        
def get_pet(pet_id):
    if pet_id:
        print (pets[pet_id])

while command != "stop":
    command = input ("Введите команду - ").lower()

    if command == "create":
        create()

    if command == "read":
        read()

    elif command == "update":
        update()

    elif command == "delete":
        delete()

    elif command == "pet_list":
        pet_list()
    
    elif command == "get_pet":
        get_pet (get_id())
    