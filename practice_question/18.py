# Check the number is amstrong or not

num = int(input("Enter a number here: "))

sum = 0
temp = num

while temp > 0:
    digit = temp%10
    cube = digit ** 3
    sum = sum + cube
    temp  //= 10
    
if sum == num :
    print("It is an amstrong number")
else:
    print("it is not an amstrong number")    