# Recusrsion call itself

'''
factorial(1) = 1
factorial(5) = 5x4x3x2x1
factorial(n) = n x n-1 X......3 x 2 x 1

factorial(n) = n * factorial(n-1)

'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input(f"The factorial of number "))
print(f"The factorial of the number is {factorial(n)}")