# Demonstrate polymorphism by defining a method fuel_type in both car and electriccar classes but with different behaviours


'''Polymorphism means "one thing, many forms." It’s like a person who behaves differently in different situations—like a teacher who teaches in class but plays with kids at home. In programming, it allows the same action to work in different ways.'''

class Car:
    def __init__(self, brand , model):
        self.__brand = brand # __ class private ho jeyegi class and andar access hoga bahar problem hogi
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # yai kaam ho chuka hai like ham uper wali class ka access kar sakte hai 
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"
    

# my_car = Car("Tata","Safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name()) 

my_tesla = ElectricCar('Tesla', "Model S","85KWH")
# print(my_tesla.brand)
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())

# my_new_car = Car("Audi","Q5")
# print(my_new_car.brand)
# print(my_new_car.model)