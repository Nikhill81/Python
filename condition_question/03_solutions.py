# Grade Calculator

grade = int(input("Emter the marks: "))

if grade >= 101:
    print("Please varify your grade agian")
    exit()


if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")    
elif grade >= 60:
    print("D grade")
else:
    print("Fail")

