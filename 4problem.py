import os

# Specify the directory you want to list
directory_path = '/'  # You can change this to '.' for current folder

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)
import os

# Set the path to the directory you want to explore
# Use "." to mean the current directory
directory = "."

# Check if it's a valid directory
if os.path.isdir(directory):
    print(f"Contents of directory '{directory}':\n")
    
    # List and print each item inside the directory
    for item in os.listdir(directory):
        print(item)
else:
    print(f"The path '{directory}' is not a valid directory.")
import os

# Set the path to the directory you want to explore
# Use "." to mean the current directory
directory = "./new folder"
# Check if it's a valid directory
if os.path.isdir(directory):
    print(f"Contents of directory '{directory}':\n")
    
    # List and print each item inside the directory
    for item in os.listdir(directory):
        print(item)
else:
    print(f"The path '{directory}' is not a valid directory.")
