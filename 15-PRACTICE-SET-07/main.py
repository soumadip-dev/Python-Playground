# Decorators in Python

"""
1: Create a decorator named logger that prints
"Function is being called" before the actual function runs.
"""


def logger(function_to_run):
    # Wrapper function that adds behavior before running the function
    def wrapper():
        print("Function is being called.")
        function_to_run()

    return wrapper


# Function that will be decorated
def say_hello():
    print("Hello!")


# Applying the decorator manually
decorated_function = logger(say_hello)
decorated_function()


"""
2: Create a decorator named timer that calculates how long
a function takes to execute. Test it with a function that
sums numbers from 1 to 1,000,000.
"""

import time


def timer(function_to_measure):
    # Wrapper function that measures execution time
    def wrapper():
        start_time = time.time()

        function_to_measure()

        end_time = time.time()

        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")

    return wrapper


# Using the decorator with @ syntax
@timer
def calculate_large_sum():
    total_sum = 0

    for number in range(1, 1_000_001):
        total_sum += number

    print("Total sum:", total_sum)


calculate_large_sum()


# Getters and Setters

"""
3: Create a class Employee with a private attribute _salary.

- Use @property to define a getter for salary.
- Use @salary.setter to prevent setting negative values.
- Print a warning if a negative value is provided.
"""


class Employee:

    def __init__(self, salary_amount):
        self._salary = salary_amount

    # Getter method
    @property
    def salary(self):
        return self._salary

    # Setter method with validation
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Warning: Salary cannot be negative.")
        else:
            self._salary = new_salary


first_employee = Employee(45000)

print("Initial salary:", first_employee.salary)

first_employee.salary = 50000
print("Updated salary:", first_employee.salary)

first_employee.salary = -5000


# Magic / Dunder Methods

"""
4: Create a class Book with attributes title and author.

- Implement __str__() so printing the object displays "Title by Author".
- Implement __len__() so len(book) returns the length of the title.
"""


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)


first_book = Book("Python Basics", "John Smith")
second_book = Book("Learning Data Science", "Emily Johnson")

print(first_book)
print(second_book)

print("Length of first book title:", len(first_book))
print("Length of second book title:", len(second_book))


# Exception Handling

"""
5: Ask the user to enter a number and handle:
- ValueError if the input is not a number
- ZeroDivisionError if dividing by zero
"""

number_to_divide = 5

try:
    user_input = int(input("Enter a number: "))
    result = number_to_divide / user_input

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as error:
    print(f"An unexpected error occurred: {error}")

else:
    print("The result is:", result)

finally:
    print("Division task completed.")


"""
6: Create a custom exception NegativeNumberError and raise it when a negative number is entered.
"""


class NegativeNumberError(Exception):
    pass


try:
    user_number = int(input("Enter a number: "))

    if user_number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    print("You entered:", user_number)

except NegativeNumberError as error:
    print("Custom Error:", error)

except ValueError:
    print("Error: Please enter a valid integer.")


# map(), filter(), and reduce()

"""
7: Use map() to convert [1,2,3,4,5] into their cubes.
"""


def calculate_cube(number):
    return number**3


numbers = [1, 2, 3, 4, 5]
cube_values = list(map(calculate_cube, numbers))

print("Cube values:", cube_values)


"""
8: Use filter() to get only even numbers from [10,11,12,13,14]
"""

numbers_list = [10, 11, 12, 13, 14]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers_list))

print("Even numbers:", even_numbers)


"""
9: Use reduce() to find the product of [1,2,3,4]
"""

from functools import reduce

numbers_for_product = [1, 2, 3, 4]

product_result = reduce(lambda x, y: x * y, numbers_for_product)

print("Product of numbers:", product_result)


# Walrus Operator

"""
10: Read input until the user enters "quit".
"""

while user_input := input("Enter a value (type 'quit' to quit): "):
    if user_input == "quit":
        print("Exiting the program.")
        break
    print("You entered:", user_input)


"""
11: Use walrus operator in list comprehension to store lengths of words
greater than 4 characters.
"""

words = ["python", "rocks", "ai"]

word_lengths = [length for word in words if (length := len(word)) > 4]

print("Lengths of words greater than 4:", word_lengths)


"""
12: Write a function sum_all(*args) that accepts any number of integers
and returns their sum.
"""


def sum_all(*numbers):
    total_sum = 0

    for number in numbers:
        total_sum += number

    return total_sum


print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))


"""
13: Write a function print_details(**kwargs) that prints key-value pairs.
"""


def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=25, city="Delhi")


"""
14: Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
"""


def universal_decorator(function_to_wrap):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = function_to_wrap(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@universal_decorator
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Soumadip")


@universal_decorator
def show_numbers(a, b, c, d, name="Souma", age=24):
    print("Numbers:", a, b, c, d)
    print("Name:", name)
    print("Age:", age)


show_numbers(1, 2, 3, 4, name="Souma", age=24)
