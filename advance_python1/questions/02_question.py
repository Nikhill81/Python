# Write a program to print third, fifth and seventh elements from a list using enumerate function.


l = [1,4,3,2,5,7]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
     print(item)

