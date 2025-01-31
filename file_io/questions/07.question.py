# Write a program to find out the line number where python is preesnt form ques 6.


with open("file_io/questions/log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:

  if("python" in line):
     print(f"Yes python is present. Line no : {lineno}")
     break
  lineno += 1   

else:
    print("python is not present")     
