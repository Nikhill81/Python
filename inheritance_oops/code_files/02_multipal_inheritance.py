class Employee:

    company = "ITC"
    name = "Defalut name"
    def show(self): 
        print(f"The name is {self.name} and the company is {self.company}")

class coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language : {self.language}")


class Programmer(Employee, coder):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company , b.company)

b.show()
b.printLanguages()
b.showLanguage()
    
# Inheritance is a way of creating a new class from an existing class