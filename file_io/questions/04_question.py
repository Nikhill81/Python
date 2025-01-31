# A File contains a word "Donkey" multipal times. You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"

with open("/Users/nikhil/Desktop/python/file_io/questions/file.txt","r") as f:
    content = f.read()

contentNew = content.replace(word, "######")
with open("/Users/nikhil/Desktop/python/file_io/questions/file.txt", "w") as f:

  f.write(contentNew)