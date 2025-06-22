# array = [2,5,3,7,8,9,6]
# input 3 = 2
# input  1 = -1
# 7 = 3


# array =  [2,5,3,7,8,9,6]
# # fact = 0
# val = int(input("enter the number here: "))

# if val > array:
#     print("Hello")

# else:
#     print("No")




# val = int(input("Enter the element here : "))

# if val in arr:
#     print(f"{val} Present {index}")
# else:
#     print(f"{val} not available")

# def print_index(array,input):
#     arr = [2, 3, 5,6, 7, 8, 9]
#     input = 3
#     first_index = 0
#     last_index = len(arr)-1
#     for value in arr:
#         if input == value:
#             return index
#         index = index+1
#     return -1

#Inheritance 

# '''Class'''
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
# '''OBCJECT'''
# my_car = Car ("Tata")
# print(my_car.brand)

# '''INHERITANCE'''
# class ElectircCar(Car):
#     def __init__(self, brand, battery):
#         super() .__init__(brand)
#         self.battery = battery
# '''Polymorphism'''
# class Bird:
#     def speak(self):
#         print("Hello")
# '''Encapsulation:'''
# class Dog:
#     def speak(self):
#         print("bark")
# for animal in (Bird(), Dog()):
#     animal.speak

# class person:
#     def __init__(self):
#         self._name = "Cognizant" # Protected
#         self.__age = 22 # private 


# '''Abstraction'''
# from abc import ABC, abstractclassmethod

# class Shape(ABC):
#     @abstractclassmethod
#     def area(self):
#         pass