# Write a program to copy a file of text file "this.txt"

with open("file_io/questions/this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)