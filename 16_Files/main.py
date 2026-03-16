# File Handling in Python

# Using try-except-finally to ensure the file is always properly closed.


# Reading a file:
# Opens the file in read mode ("r").
# This is the default mode. If the file does not exist, an error will occur.

read_file_handle = open("test.txt", "r")

try:
    file_content = read_file_handle.read()

except Exception:
    print("An error occurred while reading the file.")

finally:
    read_file_handle.close()
    print(file_content)


# Writing to a file:
# Opens the file in write mode ("w").
# If the file already exists, its content will be overwritten.
# If the file does not exist, a new file will be created.

write_file_handle = open("test.txt", "w")

try:
    write_file_handle.write("Name: Soumadip Majila")

except Exception:
    print("An error occurred while writing to the file.")

finally:
    write_file_handle.close()


# Appending to a file:
# Opens the file in append mode ("a").
# New data will be added to the end of the file.
# If the file does not exist, Python will create it.

append_file_handle = open("test.txt", "a")

try:
    append_file_handle.write(". Friend of Ram Roy")

except Exception:
    print("An error occurred while appending to the file.")

finally:
    append_file_handle.close()


# Reading a file line by line

line_reader_handle = open("test2.txt", "r")

try:
    for line in line_reader_handle:
        print(line)

except Exception:
    print("An error occurred while reading the file line by line.")

finally:
    line_reader_handle.close()


# Using the 'with' statement (recommended modern approach):
# It automatically closes the file after execution,
# even if an error occurs.

with open("test.txt", "r") as read_file_handle:
    file_content = read_file_handle.read()
    print(file_content)
