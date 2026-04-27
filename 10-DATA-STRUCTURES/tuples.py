# Tuples in Python

# A tuple is an ordered but immutable collection of elements.
# Immutable means the elements cannot be changed after the tuple is created.

numbers_tuple = (3, 2, 22, 13)

print("Tuple:", numbers_tuple)
print("First element of the tuple:", numbers_tuple[0])

# numbers_tuple[3] = 45
# This will cause an error because tuples do not support item assignment.


# Creating a single-element tuple
# If we write (10), Python treats it as a normal integer inside parentheses.
# To create a tuple with a single element, we must add a comma.

single_element_tuple = (10,)  # This correctly creates a tuple


# Tuple unpacking
# Tuple unpacking allows assigning tuple elements to multiple variables.

values_tuple = (33, 2, 45)

first_value, second_value, third_value = values_tuple

print("First value from the tuple:", first_value)


# Tuple methods

sample_tuple = (3, 12, 1, 54)

# count() returns the number of times a value appears in the tuple
print("Count of 3 in the tuple:", sample_tuple.count(3))

# index() returns the index of the first occurrence of the given value
print("Index of 12 in the tuple:", sample_tuple.index(12))
