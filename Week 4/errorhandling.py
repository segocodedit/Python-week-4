# 2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# asking the user for a filename
filename = input("Enter the filename:")

try: 
   with open(filename,'r') as file:
      content = file.read()
    

      # file doesn’t exist
except FileNotFoundError:
   print(f"Error: the file '{filename}' doesn't exist")
   
     # file can't be read
except PermissionError:
    print(f"\nError: You don't have permission to read '{filename}' ")

else: 
     print(content)
   
 




