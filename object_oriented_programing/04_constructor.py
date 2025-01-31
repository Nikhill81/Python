
class Employee:
    language = "Py" # this is a class attribute
    salary = 2000000

    def __init__(self,name,salary,language): # Dunder method which is automatically called (dunder method wo hota joo duble underscore se start hota hai)
         
         self.name = name
         self.salary = salary
         self.language = language
         print("I am creating this object")

    def getInfo(self):
        print(f"The language is {self.language} the salary is {self.salary} ")

    @staticmethod # after declearing this we dont need to call self  
    def greet():
            print("Good Morning")

John = Employee("John", 34444444, "Javascript")
# John.name = "jadhav"

print(John.name, John.salary, John.language)

#rohan = Employee()

