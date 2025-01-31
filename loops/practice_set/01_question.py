# Write a program to print multiplication table of a given number using for loop

'''
n = int(input("Enter a number: "))

for i in range(1, 11): 
    print(f"{n} x {i} = {n * i} ")

'''

# Write a program to great all the person names stored in a list "l" and which starts with s 

l = ["ritik" , "John", "vivek", "ravi"]

for name in l :
    if(name.startswith("r")):
        print(f"Hello {name}")