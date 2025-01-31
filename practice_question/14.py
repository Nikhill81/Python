'''Find the factorail of the number'''

# factorail = int(input("Enter the number here : "))

# fact = 1

# if factorail < 0:
#     print("Factorial of 0 does not exist")

# if factorail == 0:
#     print("The Factorail of 0 is 1")

# if factorail > 0:
#     for i in range(1 , factorail+1):
#         fact = fact * i
# print('The factoral of the given number is this ', fact)    
# 
#    
 

'''By Recursion method => Function ko agar function khud kai andar call karta hai tab usko recursion kehte hai function ko khud he call karne ko recursion bolte hai ''' 

def fact(a):
    if a == 0:
        return 1
    else:
        return((a)*fact(a-1))
num = int(input("Enter the number here: "))
result = fact(num)
print("The factorail of the given number is ", result)



