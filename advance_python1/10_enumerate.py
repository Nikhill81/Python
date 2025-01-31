l = [21,31,23,334,212,1]

index = 0

# for item in l:
#     print(f"The item number at index {index} is {item} ")
#     index += 1

# This can be simplyfied using enumerate function

for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")
