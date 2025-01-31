class Employee:
    language = "Py" # this is a class attribute
    salary = 2000000

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary} ")
        
    @staticmethod # after declearing this we dont need to call self  
    def greet():
            print("Good Morning")

John = Employee()
# John.language = "JavaScript" # This is an instance attribute
# print(John.language, John.salary)   
John.greet() 
John.getInfo()
 