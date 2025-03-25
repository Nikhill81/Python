class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine info"

class ElectricCarTwo(Battery, Engine):
    def __init__(self, name): 
        self.name = name  

my_new_car = ElectricCarTwo("Tesla")  
print(my_new_car.engine_info())
print(my_new_car.battery_info())
print(f"Car name: {my_new_car.name}")  
