# Function with arguments 

'''
def goodDay(name, ending):
    print(" Good Day," + name)
    print(ending)

goodDay("John", "Thank you")
goodDay("Doe", "thank ")
goodDay("milkha singh", "nice")

'''

# 

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

# If we dont use return we got none value

a = goodDay("John", "Thank You")
print(a)
