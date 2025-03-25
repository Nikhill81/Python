# def reverse_Str(S):
#     return S[::-1]
# print(reverse_Str("Hello"))


# def sum():
#     arr = [1,2,3,4,5,6]
#     add = 0
#     if arr % 2:
#         print(f"sum of even number {arr + add}")
#         return
#     print("This is odd number")
# sum(4)
# sum(3)


# -----------------------------------------------------------------------------------

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# user_input = input("Enter numbers separated by spaces: ")

# numbers = user_input.split()

# for i in range(len(numbers)):
#     day = days[i % 7]  
#     print(f"{numbers[i]} {day}")

# def print_days_with_numbers():   
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]    
#     user_input = input("Enter numbers separated by spaces: ")    
#     numbers = list(map(int, user_input.split()))
    
#     for i, num in enumerate(numbers):
#         day = days[i % 7] 
#         print(f"{day} {num}")

# print_days_with_numbers()
