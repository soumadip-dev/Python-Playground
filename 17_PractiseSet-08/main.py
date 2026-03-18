# File Handling

"""
1: Create a text file called notes.txt and write the text
   "Learning Python is fun!" into it.
"""
with open("notes.txt", "w") as file:
    file.write("Learning Python is fun!")

"""
2: Open the file notes.txt, read its content,
   and print the content to the console.
"""
with open("notes.txt", "r") as file:
    print(file.read())

"""
3: Write a program that writes three lines of text
   into a file named tasks.txt.
"""
with open("tasks.txt", "w") as file:
    file.write("Task 1\n")
    file.write("Task 2\n")
    file.write("Task 3\n")

"""
4: Open tasks.txt in append mode and add a new line:
   "Task Completed!"
"""
with open("tasks.txt", "a") as file:
    file.write("Task Completed!\n")

"""
5: Read the file tasks.txt and print all lines
   as a list using the readlines() method.
"""
with open("tasks.txt", "r") as file:
    lines = file.readlines()
    print(lines)


"""
6: Write a program that reads a file and creates another file
   where all words are converted to uppercase.
"""
with open("tasks.txt", "r") as file:
    content = file.read()

with open("tasks_uppercase.txt", "w") as new_file:
    new_file.write(content.upper())


# OS and Shutil Modules

"""
7: Use the os module to:
   - Print the current working directory.
   - List all files and folders in the current directory.
   - Create a new folder named my_folder.
"""
import os

print(f"Current working directory: {os.getcwd()}")
print(f"Files and folders in the current directory: {os.listdir()}")
os.mkdir("my_folder")

"""
8: Use the shutil module to:
   - Copy a file from one folder to another.
   - Move a file to a new folder.
   - Delete a folder (Warning: This action is irreversible).
"""
import shutil

shutil.copy("tasks.txt", "my_folder/tasks.txt")
shutil.move("tasks_uppercase.txt", "my_folder/tasks_uppercase.txt")
shutil.rmtree("my_folder")


"""
9: Write a script that deletes all .txt files from the current directory
   using the os module and the os.remove() function.
"""
import os

list_of_files = os.listdir()

for file_name in list_of_files:
    if file_name.endswith(".txt"):
        os.remove(file_name)


# Command Line Utilities

"""
10: Write a script named count_lines.py that takes a filename
    as input and prints how many lines are in the file.

    Example usage:
    python count_lines.py tasks.txt

    Expected output:
    Number of lines: 4
"""

# Create sample file for testing
with open("tasks.txt", "w") as tasks_file:
    tasks_file.write("Task 1\n")
    tasks_file.write("Task 2\n")
    tasks_file.write("Task 3\n")
    tasks_file.write("Task 4\n")


import argparse

# Create argument parser
argument_parser = argparse.ArgumentParser(
    description="Count the number of lines in a file"
)

# Add filename argument
argument_parser.add_argument("file_name", help="Enter the file name to count lines")

# Parse arguments
arguments = argument_parser.parse_args()

# Count lines in file
with open(arguments.file_name, "r") as input_file:
    line_count = 0

    for line in input_file:
        line_count += 1

print("Number of lines:", line_count)


"""
11: Write a command-line utility named search_word.py that takes two arguments:
    - A filename
    - A word to search

    The program should print how many times the word appears in the file.
"""

import argparse

argument_parser = argparse.ArgumentParser(description="Search for a word in a file")

# Add filename and word arguments
argument_parser.add_argument("file_name", help="Enter the file name to search")
argument_parser.add_argument("word", help="Enter the word to search")

arguments = argument_parser.parse_args()

with open(arguments.file_name, "r") as input_file:
    file_content = input_file.read()
    word_count = file_content.count(arguments.word)

print(f"The word '{arguments.word}' appears {word_count} times in the file.")


"""
12: Write a Python command-line tool that takes a folder name
    and prints the total size of all files inside it.

    Hint: Use os.path.getsize().
"""

import argparse

argument_parser = argparse.ArgumentParser(
    description="Calculate the total size of files in a folder"
)

argument_parser.add_argument("folder_name", help="Enter the folder name")

arguments = argument_parser.parse_args()

total_size = 0

for file_name in os.listdir(arguments.folder_name):
    file_path = os.path.join(arguments.folder_name, file_name)

    if os.path.isfile(file_path):
        total_size += os.path.getsize(file_path)

print(f"The total size of the folder is {total_size} bytes.")
