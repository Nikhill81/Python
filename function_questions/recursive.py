# Create a recursive function to calculate the factorial of a number

def factorail(n):
    if n  == 0:
        return 1
    else:
        return n * factorail(n-1)
factorail(4)