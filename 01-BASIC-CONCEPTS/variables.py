# In Python, variables are used to store data that can be used and manipulated throughout a program.
# A variable is created the moment you assign a value to it using the assignment operator (=).

age = 34            # Integer
name = "Soumadip"   # String
cgpa = 4.55         # Float
is_passed = True    # Boolean

# Python is a dynamically typed language: we don't need to explicitly define
# the type of a variable before assigning a value to it.


# Rules for defining a variable in Python

# 1. Variable names must start with a letter (a–z, A–Z) or an underscore (_).
# 2. They can contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive (age and Age are different).
# 4. Avoid using Python keywords (e.g., if, for, while) as variable names.


print(age, name, cgpa)

# We can get the type of any variable using the type() function
print(type(age))  # <class 'int'>


# Python supports several built-in data types:

# Floats (float): Decimal numbers (e.g., 3.14, -0.001).
# Integers (int): Whole numbers (e.g., 18, -5).
# Strings (str): Text data enclosed in quotes (e.g., "Hello", "Python").
# Booleans (bool): Represents True or False.
# Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
# Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
# Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
# Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).
