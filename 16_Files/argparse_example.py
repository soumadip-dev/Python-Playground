# Argparse Module Example: Simple Calculator
# This program performs basic arithmetic operations using command-line arguments.

import argparse

# Create the argument parser object with a description
argument_parser = argparse.ArgumentParser(description="Simple Calculator Program")

# Add command-line arguments
argument_parser.add_argument("first_number", type=float, help="Enter the first number")
argument_parser.add_argument(
    "second_number", type=float, help="Enter the second number"
)

argument_parser.add_argument(
    "operation",
    choices=["add", "sub", "mul", "div"],
    help="Choose the operation: add, sub, mul, or div",
)

# Parse the arguments provided by the user
arguments = argument_parser.parse_args()


# Perform the selected operation using match-case
match arguments.operation:

    case "add":
        result = arguments.first_number + arguments.second_number
        print(
            f"The sum of {arguments.first_number} and {arguments.second_number} is {result}"
        )

    case "sub":
        result = arguments.first_number - arguments.second_number
        print(
            f"The subtraction of {arguments.first_number} and {arguments.second_number} is {result}"
        )

    case "mul":
        result = arguments.first_number * arguments.second_number
        print(
            f"The multiplication of {arguments.first_number} and {arguments.second_number} is {result}"
        )

    case "div":
        if arguments.second_number == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = arguments.first_number / arguments.second_number
            print(
                f"The division of {arguments.first_number} by {arguments.second_number} is {result}"
            )
