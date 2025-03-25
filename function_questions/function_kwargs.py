# Function with **Kwargs 
# Create a function that accepts any number of keyword arguments and points them in the formet key : value


def print_kwargs(**kwargs):
    for key, value in kwargs.item():
        print(f"{key}: {value}")

print_kwargs(name="Pawan Singh", power="lazer")   
print_kwargs(name="Pawan Singh", power="lazer",enemy = "Dr. Jackaal") 