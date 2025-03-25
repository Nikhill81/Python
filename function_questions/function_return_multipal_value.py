# Crete a function that returns both the area and circumference of a circle given its radius.


# import math

# def circle_stats(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference
# a, c = circle_stats(3)
# print("Area", a , "Circumference",c)


import math

def circle_stats(radius):
    
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Input: Radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
a, c = circle_stats(radius)

# Output: Display results formatted to 2 decimal places
print(f"Area: {a:.2f}, Circumference: {c:.2f}")