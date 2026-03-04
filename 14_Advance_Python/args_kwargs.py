# *args and **kwargs in Python

from functools import reduce


# *args
# *args allows a function to accept any number of positional arguments.


def add_multiple_numbers(*numbers):

    # Helper function used by reduce to add two numbers
    def add_values(first_number, second_number):
        return first_number + second_number

    # reduce applies the add_values function cumulatively to all numbers
    total_sum = reduce(add_values, numbers)

    return total_sum


print("Sum of the given numbers:", add_multiple_numbers(342, 2, 7))


# **kwargs
# **kwargs allows a function to accept any number of keyword arguments.
# The arguments are stored as a dictionary.


def display_student_marks(**student_marks):

    # Loop through each subject and its corresponding marks
    for subject_name, marks in student_marks.items():
        print(f"{subject_name}: {marks}")


display_student_marks(math=85, english=78, science=90, history=88, computer_science=92)


# Combining *args and **kwargs
# We can use both *args and **kwargs in the same function.
# The order must be: normal parameters → *args → default parameters → **kwargs


def display_function_parameters(
    first_value, second_value, *additional_values, optional_value=10, **extra_details
):

    print(f"First value: {first_value}")
    print(f"Second value: {second_value}")
    print(f"Additional values (*args): {additional_values}")
    print(f"Optional value: {optional_value}")
    print(f"Extra details (**kwargs): {extra_details}")


display_function_parameters(
    1, 2, 3, 4, 5, 6, 7, optional_value=20, name="Bob", country="USA"
)
