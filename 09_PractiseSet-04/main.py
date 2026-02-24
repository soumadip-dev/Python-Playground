"""
1. Write a function greet() that prints "Hello, Python Learner!" when called.
"""


def greet():
    """Prints a greeting message for Python learners."""
    print("Hello, Python Learner!")


greet()


"""
2. Write a function square(number) that returns the square of a given number.
"""


def square(number):
    """Returns the square of the given number."""
    return number**2


print("The square of 5 is:", square(5))
print("The square of 6 is:", square(6))


"""
3. Write a function get_full_name(first_name, last_name)
   that returns a full name in the format 'First Last'.
"""


def get_full_name(first_name, last_name):
    """Returns the full name by combining first name and last name."""
    return f"{first_name} {last_name}"


print("Full name:", get_full_name("Soumadip", "Majila"))


"""
4. Write a function calculate_area(length, width=10)
   that returns the area of a rectangle.
"""


def calculate_area(length, width=10):
    """Calculates the area of a rectangle."""
    return length * width


print("Area with length 5 and width 4:", calculate_area(5, 4))
print("Area with length 5 and default width:", calculate_area(5))


"""
5. Write a lambda function that adds two numbers.
"""

add_numbers = lambda first_number, second_number: first_number + second_number
print("The sum of 1 and 2 is:", add_numbers(1, 2))


"""
6. Use map() with lambda to calculate the square of numbers in a list.
"""

numbers_list = [1, 2, 3, 4, 5]

squared_numbers_list = list(map(lambda number: number**2, numbers_list))

print("Original numbers:", numbers_list)
print("Squared numbers:", squared_numbers_list)


"""
7. Write a recursive function factorial(number)
   that returns the factorial of a number.
"""


def factorial(number):
    """Calculates factorial using recursion."""
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


print("Factorial of 4 is:", factorial(4))


"""
8. Write a recursive function sum_of_digits(number)
   that returns the sum of all digits.
"""


def sum_of_digits(number):
    """Returns the sum of digits using recursion."""
    if number == 0:
        return 0
    return number % 10 + sum_of_digits(number // 10)


print("Sum of digits in 102:", sum_of_digits(102))


"""
9. Use the math module to:
   - Find the square root of 144
   - Calculate sin(90 degrees)
"""

import math

square_root_value = math.sqrt(144)
sine_value = math.sin(math.radians(90))

print("Square root of 144:", square_root_value)
print("Sine of 90 degrees:", sine_value)


"""
10. Use the requests module to fetch data from the GitHub API.
"""

import requests

response = requests.get("https://api.github.com")
github_data = response.json()

print("GitHub API response:")
print(github_data)


"""
11. Demonstrate local variables inside a function.
"""


def increment():
    """Demonstrates that local variables reset in each function call."""
    counter = 1
    counter += 1
    print("Counter value inside the function:", counter)


increment()
increment()
increment()


"""
12. Write a function multiply(a, b) with a proper docstring.
"""


def multiply(first_number, second_number):
    """
    multiply(first_number, second_number)

    Returns the product of two numbers.

    Parameters:
    first_number (int or float): The first number
    second_number (int or float): The second number
    """
    return first_number * second_number


help(multiply)


"""
13. Write a recursive function that prints the first n Fibonacci numbers.
"""


def fibonacci(total_numbers):

    def fib(number):
        if number <= 1:
            return number
        return fib(number - 1) + fib(number - 2)

    for index in range(total_numbers):
        print(fib(index), end=" ")


fibonacci(10)
print()


"""
14. Write a function safe_divide(a, b) that safely divides two numbers.
"""


def safe_divide(first_number, second_number):
    """Returns the result of division or a message if division by zero occurs."""
    if second_number == 0:
        return "Cannot divide by zero"
    return first_number / second_number


print(safe_divide(30, 10))
print(safe_divide(3, 0))


"""
15. Import and use a custom module named my_utils.
"""

import my_utils

test_number = 10

if my_utils.is_even(test_number):
    print("The number is even.")
else:
    print("The number is odd.")
