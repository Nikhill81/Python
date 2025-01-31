try:
    a = int(input("Enter a number here: "))
    print(a)

except Exception as e:
    print(e)
    print("Heyyyy")
    
except ValueError as v:
    print(v)    

print("Thank You")    

# exception handling mechanism is used to deal with unexpected errors or exceptional situations that occur during the execution of a program