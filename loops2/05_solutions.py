# Find the First Non-Repeated Charecter :Given a string and find the first non repeated character.

input_str = "preepirrt"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is ", char)
        break
