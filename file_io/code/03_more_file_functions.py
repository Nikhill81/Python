f = open("/Users/nikhil/Desktop/python/file_io/file.txt")

#lines = f.readlines()
#print(lines, type(lines))

#
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))


''''
line5 = f.readline()
print(line5 =="")

# If you ask for extra line which was not existed it shows nothing no error it return empty string which we can see through using print(line5 =="") this method

'''

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()




