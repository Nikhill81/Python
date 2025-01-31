from functools import reduce
# Map Example (agar hamko ek function chalana hai sare element kai liye  )

l = [1,2,4,5,6]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))


# Filter Example:

def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

# Reduce Example


def sum(A,b):
    return A + b
mul = lambda x,y:x*y
print(reduce(sum, l))
print(reduce(mul, l))