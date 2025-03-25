# Add a static method to the car class that returns a general description of a car.

class Car:
    total_car = 0

    def __init__(self, brand , model):
        self.__brand = brand # __ class private ho jeyegi class and andar access hoga bahar problem hogi
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
     
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod #decorators
    def general_discription():
        return "cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # yai kaam ho chuka hai like ham uper wali class ka access kar sakte hai 
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"
    

my_car = Car("Tata","Safari")
print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name()) 

#my_tesla = ElectricCar('Tesla', "Model S","85KWH")
# print(my_tesla.brand)
#print(my_tesla.fuel_type())

print(my_car.general_discription())
print(Car.general_discription())


safari = Car("Tata","Safari")
safariThree = Car("Tata","Nexon")
print(safari.fuel_type())

print(Car.total_car)

# my_new_car = Car("Audi","Q5")
# print(my_new_car.brand)
# print(my_new_car.model)