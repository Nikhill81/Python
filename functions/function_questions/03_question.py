
# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4+5

sum(n) = 1+2+3+4....n -1 + n
sum(n) = sum(n-1) + n
'''

'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))

'''

#----------------------------------------------

# Write a python function to print multiplication table of a given number.

def multiply(n):
    for i in range (1, n+11):
        print(f"{n} X {i} = {n*i}")

multiply(6)        
