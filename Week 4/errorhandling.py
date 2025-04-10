# try:  
#  with open('tests.txt') as f:
#     print(f.read())
# except: 
#    print("File was not found")


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
   
 




