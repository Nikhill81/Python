a = int(input("Enter a number here: "))
b = int(input("Enter a number here: "))

if(b == 0):
    raise ZeroDivisionError("Hey you can't divide by zero ")

else:
    print(f"Your divison is {a/b}")