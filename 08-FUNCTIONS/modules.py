# Modules in Python

# 1. Internal (Built-in) Modules
# These modules are included with Python by default.

import math

square_root_value = math.sqrt(16)
print("Square root of 16:", square_root_value)


# 2. External Modules
# External modules are installed using pip.

# Example:
# pip install requests

import requests

response = requests.get(
    "https://www.google.com"
)  # Returns the HTML response of the given URL
print("HTTP response status:", response)


# 3. User-defined Modules
# These modules are created by the programmer.

import my_module

my_module.hello()
