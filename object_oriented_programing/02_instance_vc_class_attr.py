class Employee:
    language = "Py" # this is a class attribute
    salary = 2000000

John = Employee()
John.language = "JavaScript" # This is an instance attribute
print(John.language, John.salary)    

