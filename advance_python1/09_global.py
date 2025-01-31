# a = 100

# # Global keyword can change the global variables 

# def function():
#     global a
#     a = 3
#     print(a)

# function()
# print(a)

a = 100
def function():
    global a
    a = 3
    print(a)
function()
print(a)
