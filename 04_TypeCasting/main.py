# Typecasting is the process of converting one data type to another.

a = 34
b = "34"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>

# Python provides built-in functions for typecasting:

# Convert string b to an integer
c = int(b)
print(c)
print(type(c))  # <class 'int'>

# Convert integer a to a string
e = str(a)
print(e)
print(type(e))  # <class 'str'>

# Convert integer a to a float
f = float(a)
print(f)
print(type(f))  # <class 'float'>

# Convert string b to a boolean
g = bool(b)
print(g)
print(type(g))  # <class 'bool'>
