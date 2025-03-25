'''First Method'''

# str = "Python"
# print(str[-1::-1])

'''Second Method'''

a = input('Enter a string')
for i in range((len(a)-1),-1,-1):
    print(a[i],end="")