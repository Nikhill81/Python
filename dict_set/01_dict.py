
marks = {
    "ritesh": 100,
    "rtiki": 42,
    "Rohan": 32,
    2: "shivam"
}

# print(marks,type(marks))

#print(marks.items())
#print(marks.keys()) # values 

marks.update({"ritik": 99})
#print(marks)

print(marks.get("rohan")) # Prints none
print(marks["Harry"]) # returns error

# it is ordered
# it is mutable
# it is indexed 
# cant containe duplicate keys

