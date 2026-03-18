# Shutil Module in Python
# The shutil module provides high-level file operations such as copying,
# moving, and removing directories with their contents.

import shutil


# Remove a directory and all its contents recursively
# This will delete the directory even if it contains files and subdirectories.
shutil.rmtree("dir")


# Copy a file from one location to another
# Here, test2.txt is copied and renamed as file2.txt
shutil.copy("test2.txt", "file2.txt")


# Move a file from one location to another
# This will move test2.txt to the specified directory.
# If the destination exists, the file will be placed inside it.
shutil.move("test2.txt", "../dir")
