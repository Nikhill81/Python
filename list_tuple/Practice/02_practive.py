# Write a program to accept marks of 6 students and display them in a stored manner .

marks = []

m1 = int(input("Marks of student "))
marks.append(m1)
m2 = int(input("Marks of student "))
marks.append(m2)
m3 = int(input("Marks of student "))
marks.append(m3)
m4 = int(input("Marks of student "))
marks.append(m4)
m5 = int(input("Marks of student "))
marks.append(m5)
m6 = int(input("Marks of student "))
marks.append(m6)

marks.sort()
print(marks)
