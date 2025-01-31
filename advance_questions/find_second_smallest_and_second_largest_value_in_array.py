n = int(input("Enter the total number of element you want to inside the list: "))
l = []

for i in range(n):
    element = int(input("Enter the element here: "))
    l.append(element)

print("My List: ", l)    
shorted_list = l.sort()

print("Shorted List: ",l)
minimum_element =l[0]
print("Minimum Element: ",minimum_element)

maximum_element = l[-1]
print("Maximum Element: ", maximum_element)

second_largest = l[-2]
print("Second largest number: ", second_largest)