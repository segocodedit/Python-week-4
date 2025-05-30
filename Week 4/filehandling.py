## File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# Create new file using 
try:  
 with open('myfile.txt','x') as f:
    print(f.read())
except FileExistsError: 
   print("File already exists")

# write in the new file
with open('myfile.txt','a') as f:
    f.write("I love cake \n")

# Read the new file 
with open('myfile.txt','r') as f:
   print(f.read())

# Write a modified version to a new file.
with open("myfile.txt") as f:
  content = f.read()

with open("modify.txt", "w") as f:
  f.write(content)




