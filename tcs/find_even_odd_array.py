# program to print sum of even and odd element in array
def sum_even_odd(arr):
    even_sum = 0
    odd_sum = 0

    for num in arr:        
        if num % 2 == 0:  
            even_sum = even_sum + num 
        else: 
            odd_sum = odd_sum + num
    
    print("Sum of even elements:", even_sum)
    print("Sum of odd elements:", odd_sum)

arr = [1, 2, 3, 4, 5, 6]
sum_even_odd(arr)

