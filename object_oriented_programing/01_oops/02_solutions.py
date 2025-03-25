# Add a method to the Car class that displays the full name of the car (brand and model)

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Tata","Innova")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name()) # if we dont use () it will gave an error

my_new_car = Car("Audi","Q5")
print(my_new_car.brand)
print(my_new_car.model)

#  We call init as constructor