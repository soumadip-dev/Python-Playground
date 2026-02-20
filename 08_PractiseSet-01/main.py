"""
Q1: Your First Program
Write a program that prints a welcome message.
"""

print("Hello, World! Welcome to Python.")


"""
Q2: Print a Poem
Write a program that prints the following poem using a single print() statement:

Twinkle, twinkle, little star,
How I wonder what you are!
"""

print("Twinkle, twinkle, little star,\nHow I wonder what you are!")


"""
Q3: Variables and Data Types
Create variables to store:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- A boolean value representing whether you are a student

Print all of them in one line.
"""

person_name = "Soumadip"
person_age = 24
height_in_meters = 1.75
is_student = True

print(
    "My name is",
    person_name,
    "| Age:",
    person_age,
    "| Height (in meters):",
    height_in_meters,
    "| Student:",
    is_student,
)


"""
Q4: Typecasting Practice
You are given a string:

num = "45"

Convert it into an integer, add 10 to it, and print the result.
"""

number_string = "45"
number_integer = int(number_string)
result_after_addition = number_integer + 10

print("Result after adding 10:", result_after_addition)


"""
Q5: Taking User Input
Write a program that:
1. Asks the user for their favorite food.
2. Prints: Wow! I also like <food>
"""

favorite_food = input("What is your favorite food? ")
print("Wow! I also like", favorite_food)


"""
Q6: Simple Calculator
Write a program that:
1. Takes two numbers as input from the user.
2. Prints their sum, difference, product, and quotient.
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Sum:", first_number + second_number)
print("Difference:", first_number - second_number)
print("Product:", first_number * second_number)
print("Quotient:", first_number / second_number)


"""
Q7: Escape Sequences
Print the following output using escape sequences.
"""

print(
    'Harry said, "Python is awesome!"\nThis is on a new line.\tThis line starts after a tab.'
)


"""
Q8: Operator Challenge
Write a program that:
1. Takes an integer as input from the user.
2. Prints the square and cube of that number.
"""

integer_input = int(input("Enter an integer: "))

square_value = integer_input**2
cube_value = integer_input**3

print("Square:", square_value)
print("Cube:", cube_value)


"""
Q9: Quick Quiz (True/False)
Mark True or False:
"""

# 1. Python code must always end with a semicolon → False
# 2. The # symbol is used for comments in Python → True
# 3. "123" and 123 are the same in Python → False
# 4. The * operator is used for multiplication → True
# 5. \n creates a new line → True
# 6. Variables in Python can start with numbers → False
# 7. int("10") + 5 gives 15 → True
