# 1. a program that reads a file and writes a modified version to a new file.

def read_and_write_file(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()
        
        new_file = file.split('.')[0] + '_modified.' + file.split('.')[1]
        
        with open(new_file, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {new_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

file = input("Enter a file: ")

import os
if os.path.exists(file):
    read_and_write_file(file)
else:
    print("File not found, try again.")



# 2. Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

    import os

def ask_for_file():
    while True:
        file = input("Enter name of file: ")        

        if os.path.exists(file):
            try:

                with open(file, 'r') as file:
                    print(f"File '{file}' found and can be read.")
                    return file
            except PermissionError:
                print(f"Error: Permission denied to read file '{file}'.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"Error: File '{file}' not found. Please try again.")

file = ask_for_file()
print(f"You entered: {file}")