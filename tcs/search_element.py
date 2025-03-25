# def search_element(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:  
#             return f"Element {target} found at index {i}"
    
#     return f"Element {target} not found in the array"

# arr = [10, 20, 30, 40, 50]
# target = 30
# print(search_element(arr, target))  


#  
# def find_element():
#     n = 6
#     arr = [6,7,9,5,3,10]
#     k = 10
#     ans = -1

#     for i in range(n):
#         if arr[i] == k:
#             ans = i
#             break

#         print(f"The element is present in {ans} index")

# find_element()




#  bineary search

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2  # Calculate the middle index

#         if arr[mid] == target:  # Check if the middle element is the target
#             return f"Element {target} found at index {mid}"
#         elif arr[mid] < target:  # Search the right half
#             left = mid + 1
#         else:  # Search the left half
#             right = mid - 1

#     return f"Element {target} not found in the array"

# Example usage
# arr = [10, 20, 30, 40, 50]
# target = 30
# print(binary_search(arr, target))  # Output: Element 30 found at index 2

