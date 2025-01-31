# Create a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary,pin):
        self.name = name 
        self.salary = salary
        self.pin = pin

p = Programmer("Vinod", 43221,32423)
print(p.company, p.name ,p.salary,p.pin)
r = Programmer("Vikram", 12312312, 12321)
print(r.company, r.name ,r.salary,r.pin)




