# Virtual Environments in Python

# Virtual environments help isolate project dependencies and prevent conflicts
# between different Python projects. A virtual environment is a self-contained
# directory that contains its own Python interpreter and installed libraries.
# Libraries installed in one virtual environment do not affect others.


# Create a virtual environment:
# Command:
# python -m venv <environment_name>


# Activate the virtual environment:

# For Windows (PowerShell):
# .\<environment_name>\Scripts\activate

# For macOS/Linux:
# source <environment_name>/bin/activate


# Deactivate the virtual environment:
# Command:
# deactivate


# Install a package inside the virtual environment:
# Command:
# pip install <package_name>


# Show all installed packages:
# Command:
# pip list


# Upgrade a package:
# Command:
# pip install --upgrade <package_name>


# Uninstall a package:
# Command:
# pip uninstall <package_name>


# Generating a requirements file:
# A requirements file lists all the packages your project depends on.
# This makes it easy to recreate the same environment on another machine.


# Show all installed packages with versions:
# Command:
# pip freeze


# Store the package list in a requirements file:
# Command:
# pip freeze > requirements.txt


# Install all packages from a requirements file:
# Command:
# pip install -r requirements.txt
