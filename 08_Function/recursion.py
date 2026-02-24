# Recursion in Python Functions

"""
Fibonacci Series Example:

0, 1, 1, 2, 3, 5, 8, 13, ...

Explanation:
fib(0) = 0
fib(1) = 1

For any number greater than 1:
fib(n) = fib(n-1) + fib(n-2)
"""


def fibonacci(number):
    """
    This function returns the nth Fibonacci number using recursion.
    """

    # Base case of recursion
    if number == 0 or number == 1:
        return number

    # Recursive case
    return fibonacci(number - 1) + fibonacci(number - 2)


# Calculate the 7th Fibonacci number
result = fibonacci(7)

print("The 7th Fibonacci number is:", result)
