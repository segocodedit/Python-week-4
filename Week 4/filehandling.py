## File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# Create new file using with
try:  
 with open('myfile.txt','x') as f:
    print(f.read())
except FileExistsError: 
   print("File already exists")

# write in the new file
with open('myfile.txt','a') as f:
    f.write("I love cake \n")

# Read in the new file 
with open('myfile.txt','r') as f:
   print(f.read())

# Write a modified version to a new file.
with open("myfile.txt") as f:
  content = f.read()

with open("modify.txt", "w") as f:
  f.write(content)


## 2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# ask user for filename
filename = input("Enter the filename:")

try: 
   with open(filename,'r') as file:
      content = file.read()
      print.content
      # file doesn’t exist
except FileNotFoundError:
   print(f"Error: the file '{filename}' doesn't exist")
     # file can't be read
except PermissionError:
    print(f"\nError: You don't have permission to read '{filename}' ")
 



