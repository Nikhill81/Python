# Modify the car class to encapulate the brand attribute , making it private, and provide a getter method for it.

'''Encapsulation is like a school bag. It keeps books, pens, and other items together, but you can only take out what is needed through the zipper. It protects the things inside and controls how they are used. '''

class Car:
    def __init__(self, brand , model):
        self.__brand = brand # __ class private ho jeyegi class and andar access hoga bahar problem hogi
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # yai kaam ho chuka hai like ham uper wali class ka access kar sakte hai 
        self.battery_size = battery_size


# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name()) 

my_tesla = ElectricCar('Tesla', "Model S","85KWH")
# print(my_tesla.brand)
print(my_tesla.get_brand())

# my_new_car = Car("Audi","Q5")
# print(my_new_car.brand)
# print(my_new_car.model)