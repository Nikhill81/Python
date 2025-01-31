
class Employee:
    language = "Py" # this is a class attribute
    salary = 2000000

John = Employee()
John.name = "John" # This is an object attribute
print(John.name,John.language, John.salary)    

rohan = Employee()
rohan.name = "rohan goplani"
print(rohan.name,rohan.salary, rohan.language)



class EmployeeName:
    language = "python"
    salary = 1200000

John  = EmployeeName()
John.name = "John"
print(John.name , John.salary, John.language)

vinod = EmployeeName()
vinod.name = "vinod"
print(vinod.name, vinod.salary, vinod.language )

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class


'''
class Employee:
    language = "Python"
    salary = 300000

    salaryrohan = 345321
    languagerohan = "Java"

Rajiv = Employee()
print(Rajiv.language, Rajiv.salary)

Rohan = Employee()
print(Rohan.salaryrohan,Rohan.languagerohan)

'''
