# Leap Year Checker

year = int((input("Enter the year: ")))

if (year % 400 == 0) and (year % 100 == 0):
    print(year,"This is a leap year")

elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"This is a leap year")    

else:
    print(year,"This is not a leap year")    