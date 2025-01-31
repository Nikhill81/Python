# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self,a ,b):
        self.a = 1
        self.b = 2
    def show(self):
        print(f"The vector of a{self.a} is {self.b} b: ")

class ThreeDVector(TwoDVector):
    def __init__(self, a, b, c):
        super().__init__(a, b) 
        self.c = c

    def show(self):
        print(f" The vector is a {self.a} b is {self.b} and c is {self.c} ")

a = TwoDVector(1,2)
a.show()

b = ThreeDVector(1,2,3)
b.show()


