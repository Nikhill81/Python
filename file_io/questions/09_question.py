# Write a program to find out whether a file is identical & matches the content of another file

with open("file_io/questions/file.txt") as f:
    content1 = f.read()

with open("file_io/questions/poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Print yes these files are identical")

else:
    print("No these files are not identical")    