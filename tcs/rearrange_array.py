# def rearrange_array(nums):
#     positives = []
#     negatives = []
    
#     for num in nums:
#         if num > 0:
#             positives.append(num)
#         else:
#             negatives.append(num)
    
#     result = []   
#     for i in range(len(positives)):
#         result.append(positives[i])
#         result.append(negatives[i])    
#     return result

# nums = [3, 1, -2, -5, 2, -4]
# print(rearrange_array(nums))  

def rearrange(nums):
    p = []
    n = []

    for num in nums:
        if num > 0:
            p.append(num)
        else:
            n.append(num)
    result = []
          
    for i in range(len(p)):
        result.append(p[i])
        result.append(n[i])
    return result
nums = [3, 1, -2, -5, 2, -4]
print(rearrange(nums))
