# Write a program which finds wheather a given username cotains less than 10 cheracters or not

'''
username = input("Enter username")

if(len(username)<10):
    print("Your username contains less than 10 charecters")

else: 
    print("Your username contains equal to or more than 10 charecters")
'''

# Write a program which finds out whether a given name is present in a list or not.

'''
name = ["ravi", "sohan", "priya"]

a = input("Enter your name")

if (a in name ):
    print("Your name is in the list")

else:
    print("Your name is not in the list")    

'''

# Write a program to calculate the grade of a student from his marks from the following scheme

'''
90-100 => Ex
80-90 => A
70-80 => B
60-70 => C
50-60 => D
<50   => F

'''

'''
marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"

elif(marks<90 and marks>=0):
    grade = "A"    

elif(marks<80 and marks>=0):
    grade = "B"    

elif(marks<70 and marks>=0):
    grade = "C"    

elif(marks<60 and marks>=0):
    grade = "D"    

elif(marks<50 and marks>=0):
    grade = "F"   

print("Your grade is:", grade)
 
'''


# Write a program to find out wheather a given post is talking about "John" or not

post = input("Enter the post: ")

if("John".lower() in post.lower()):
    print("This post is talking about John")

else:
    print("This post is not talkig about John")    
