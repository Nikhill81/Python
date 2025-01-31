# write a python program to rename a file to "renamed_by_python.txt"

with open("file_io/questions/old.txt") as f:
    content = f.read()

with open("file_io/questions/renamed_by_python.txt", "w") as f:
   f.write("")

