
# Super() method is used to access the methods of a super class in the derived class

class Employee:
    def __init__(self):
        print("Contructor of Employee")
    a = 1

class Programmer (Employee):
    def __init__(self):
        print("Contructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Contructor of Manager")
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
#print(o.b) # Shows an error there is no b attribute in employee class

o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a, o.b, o.c)
