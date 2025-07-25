# value = int(input('Enter the number: '))
# factorial = 1

# if factorial < 0:
#     print("This is invalid factorail")
# if factorial <= 0:
#     print("facorial of 0 is 1")
# else:
#     for i in range(1, value+1):
#         factorial = factorial*i
#     print("The factoria of this number is: ", factorial)    

# ------------------------------------------------

def factorial():
    n = int(input("Enter the number: "))
    if n < 0:
        print("Error")
    elif n == 0:
        print("1")
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        print("Factorail of this number is: ", fact)
factorial()           


# class factorail():
#     def __init__(self, Num):
#         if Num < 0:
#             print("This is invalid number")
#         else:
#             fact = 1
#             for i in range(1, Num+1):
#                 fact = fact * i
#         print("The factorail of the number is", fact)
# factorail(4)



