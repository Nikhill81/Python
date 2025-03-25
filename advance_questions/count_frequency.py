
a = []
size = int(input("Enter size of the list: "))

for i in range(size):
    val = int(input("Enter Number: "))
    a.append(val)
key = int(input("Enter number to find frequency: "))
count = 0
for i in range(size):
    if(a[i]==key):
        count = count+1 
print("Frequenc =",count)          


# Another approch

# def Frequency(arr, n):
#     mp = {}
#     for i in range(n):
#         if arr[i] in mp:
#             mp[arr[i]] += 1
#         else:
#             mp[arr[i]] = 1
#     for x in mp:
#         print(x, mp[x])


# if __name__ == '__main__':
#     arr = [10, 5, 10, 15, 10, 5]
#     n = len(arr)
#     Frequency(arr, n)