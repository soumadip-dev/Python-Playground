# Example of Local and Global Variables in Python


def add_numbers(first_number, second_number):
    """
    This function adds two numbers and returns the result.
    'first_number' and 'second_number' are local variables.
    """
    sum_result = first_number + second_number
    return sum_result


print("Sum of the numbers:", add_numbers(4, 6))

# print(sum_result)
# This would cause an error because 'sum_result' is a local variable.
# Local variables exist only inside the function where they are created.


# Global variable
multiplier = 8
# A global variable can be accessed anywhere in the program.


def multiply_with_global(number):
    """
    This function multiplies the given number with the global variable 'multiplier'.
    """
    multiplication_result = number * multiplier
    return multiplication_result


print("Multiplication result:", multiply_with_global(5))


def reset_global_value():
    """
    This function modifies the global variable 'global_counter'.
    """
    global global_counter
    print("Executing the reset_global_value function.")
    global_counter = 0


global_counter = 3
print("Value of global_counter before calling the function:", global_counter)

reset_global_value()  # This changes the value of the global variable

print("Value of global_counter after calling the function:", global_counter)


# Docstrings:
# Docstrings are used to document functions, classes, and modules.
# In Python, they are written using triple quotes (""" """).
# They can be accessed using the __doc__ attribute.


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


print("Docstring of the function:", add.__doc__)
