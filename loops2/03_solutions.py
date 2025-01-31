# Multiplication Table Printer : Problem: print the multiplicaton table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter the number here : "))

for i in range(1,11):
    if i == 5:
        continue
    print(num, 'x' , i , num*i)