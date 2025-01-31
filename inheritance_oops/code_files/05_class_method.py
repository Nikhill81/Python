
# class method is a way to access class in a method

class Employee:
    a = 1
    @classmethod # it is a decorator which can we used to create a class method. (if we dont use this we get 45 in output )
    def show(cls):
        print((f"The class attribute of is {cls.a}"))
e = Employee()
e.a = 45       


e.show()