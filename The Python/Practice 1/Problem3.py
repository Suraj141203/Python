# Here We Are Using os Module its Give You info about Your Directory 
# How Many Files Insides Your Given Directory
import os

# Replace this with the path of the directory you want to list
path = "C:\\"

try:
    # Get list of all files and directories in the specified path
    contents = os.listdir(path)

    print(f"Contents of '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")
except PermissionError:
    print("Permission denied! Cannot access this directory.")
