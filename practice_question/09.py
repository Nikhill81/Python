# Find the largest among three number 

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))

if (a>b and b>a):
    print("a is largest number")

if (b>a and b>c):
    print("b is the largest number") 

if (c>a and c>b):
    print("c is the largest number")

else:
    print("Program Executed")
