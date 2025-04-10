# 2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# asking the user for a filename
while True:
    try:
        # Ask user for input
        filename = input("Enter the name of the file: ")
        with open(filename, 'r') as file:
            content = file.read()

            # file doesn’t exist error
    except FileNotFoundError:
        print(f"Error: The file '{filename}' doesn't exist. Please try again.")

         # file can't be read
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'. Please try another file.")
    else:
        print(f"Contents of file '{filename}': ")
        print(content)
        break  # Exit the loop when the file is successfully read




