# Check the number weather it is prime number or not

# num = int(input("Enter the number here: "))
# if num == 1:
#     print("It is not a prime number")
# if num > 1:
#         for i in range (2, num):
#             if num % i == 0:
#                 print("It is not a prime number")
#                 break
#         else:
#             print("It is a prime number")


def prime_num():
    n = int(input("Enter a number: "))
    if n <= 1:
        print("This is not a prime number: ")
        return
    for i in range(2, n):
        if n % i == 0:
            print("This is not prime number")
            return
        
    print("This is prime number")

prime_num()
