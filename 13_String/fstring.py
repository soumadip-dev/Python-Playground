# F-Strings in Python (Formatted Strings)

# F-strings allow variables and expressions to be embedded directly
# inside a string using curly braces {}.
# The string must start with the letter 'f'.

student_name = "Soumadip"
student_age = 23

# Printing variables inside a formatted string
print(f"My name is {student_name} and I am {student_age} years old.")


# Using expressions inside f-strings

first_number = 10
second_number = 5

# Mathematical expressions can be evaluated directly inside the braces
print(f"The sum of the numbers is {first_number + second_number}.")
print(f"The product of the numbers is {first_number * second_number}.")
