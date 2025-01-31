try:
    a = int(input("Enter a number here: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")    

# Try else ke andar tabhi execute hoga jab usme error nhi hoga


# Without try, an error would stop the program.
# With try, we can handle errors without terminating the program unexpectedly.
