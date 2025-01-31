# Write a program to read the text form a given file `poems.txt` and find out wheather it contains the word 'twinkle'

f = open("/Users/nikhil/Desktop/python/file_io/questions/poem.txt")
content = f.read()

if("twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")

f.close()