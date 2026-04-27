# OS Module in Python
# The os module provides functions to interact with the operating system.

import os


# List all files and directories in a given path
directory_contents = os.listdir("../14_Advance_Python")
print(directory_contents)


# Get the current working directory
current_working_directory = os.getcwd()
print(current_working_directory)


# Check if a file or directory exists
file_exists = os.path.exists("test.txt")
print(file_exists)


# Remove a file
# This will delete the file permanently.
# It will raise an error if the file does not exist.
os.remove("test.txt")


# Remove a directory
# This only works if the directory is empty.
# If the directory contains files, it will raise an error.
# It will raise an error if the directory does not exist.
os.rmdir("test")
