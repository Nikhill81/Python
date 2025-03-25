# Create an ElectricCar Class the inherits from the car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # yai kaam ho chuka hai like ham uper wali class ka access kar sakte hai 
        self.battery_size = battery_size


# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name()) 

my_tesla = ElectricCar('Tesla', "Model S","85KWH")
print(my_tesla.full_name())

# my_new_car = Car("Audi","Q5")
# print(my_new_car.brand)
# print(my_new_car.model)