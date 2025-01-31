# Repeat program 4 for a list of such words to be censored

words = ["Lion", "bad", "good"]

with open("/Users/nikhil/Desktop/python/file_io/questions/file.txt","r") as f:
    content = f.read()

for word in words:
 content = content.replace(word, "#" * len(word))
with open("/Users/nikhil/Desktop/python/file_io/questions/file.txt", "w") as f:

  f.write(content)