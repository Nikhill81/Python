def fizzBuzz(n):
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

n = int(input("Enter a number: "))
print(fizzBuzz(n))



# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     if i % 15 == 0:        # Check if divisible by 3 AND 5 (like 15)
#         print("FizzBuzz")
#     elif i % 3 == 0:       
#         print("Fizz")
#     elif i % 5 == 0:      
#         print("Buzz")
#     else:                  
#         print(i)