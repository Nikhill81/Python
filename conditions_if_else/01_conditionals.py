
a = int(input("Enter your age: "))

if (a>=18):
    print("You are above the age of consent")
    print("Good for you")
 
elif(a<0):
    print("Your are entering an invalid negative age ")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("you are below the age of consent") 

print("End of the program") 
