# Basic Function Example


# This function calculates and prints the average of three numbers.
def calculate_average(
    number1, number2, number3
):  # number1, number2, number3 are parameters
    average_value = (number1 + number2 + number3) / 3
    print("Average value:", average_value)


calculate_average(3, 5, 4)  # 3, 5, 4 are arguments
calculate_average(5, 9, 8)


# Function with a return statement
# This function calculates and returns the sum of three numbers.


def calculate_sum(number1, number2, number3):
    total_sum = number1 + number2 + number3
    return total_sum


sum_result1 = calculate_sum(3, 5, 4)
sum_result2 = calculate_sum(5, 9, 8)

print("Sum result 1:", sum_result1)
print("Sum result 2:", sum_result2)


# Function Arguments

# 1. Positional Arguments
# In positional arguments, values are assigned to parameters based on their order.


def multiply_numbers(number1, number2):
    product = number1 * number2
    return product


multiplication_result = multiply_numbers(4, 5)
print("Multiplication result:", multiplication_result)


# 2. Default Arguments
# A default value is used if no argument is provided.


def greet_user(user_name="Guest"):
    greeting_message = f"Hello, {user_name}!"
    return greeting_message


print(greet_user())  # Output: Hello, Guest!
print(greet_user("Soumadip"))  # Output: Hello, Soumadip!


# 3. Keyword Arguments
# In keyword arguments, parameters are passed using their names.


def display_student_details(student_name, student_age):
    print(f"Student Name: {student_name}, Age: {student_age}")


display_student_details(student_age=20, student_name="Bob")


# Lambda Function
# A lambda function is a small anonymous function defined in a single line.

square_number = lambda number: number * number
print("Square of the number:", square_number(4))

add_numbers = lambda number1, number2: number1 + number2
print("Sum of two numbers:", add_numbers(1, 2))
