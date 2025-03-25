# Create a car class with attributes like brand and model. Then careate an instance of the class

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Tata","Nexon")
print(my_car.brand)
print(my_car.model) 

my_new_car = Car("Audi","Q5")
print(my_new_car.brand)
print(my_new_car.model)