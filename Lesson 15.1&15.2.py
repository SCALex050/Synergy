#задание 15.1, 15.2

class transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров."
    
autobus = transport("Renault Logan", 180, 12)

print (f"Название автомобиля - {autobus.name}. Скорость: {autobus.max_speed}. Пробег: {autobus.mileage}.")

print (autobus.seating_capacity (50))