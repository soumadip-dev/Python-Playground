# Arithmetic Operators in Python

first_number = 10
second_number = 5
third_number = 4
base_number = 5
exponent_value = 5

print("The addition of 1 and 5 is:", 1 + 5)  # Addition
print("The subtraction of 10 and 5 is:", first_number - second_number)  # Subtraction
print(
    "The multiplication of 10 and 10 is:", first_number * first_number
)  # Multiplication
print(
    "The division of 10 by 5 is:", first_number / second_number
)  # Division (returns a float)
print("The modulus of 10 and 4 is:", first_number % third_number)  # Modulus (remainder)
print("5 raised to the power of 5 is:", base_number**exponent_value)  # Exponentiation
print(
    "The floor division of 5 by 3 is:", 5 // 3
)  # Floor division (returns integer quotient)


# Comparison Operators

number_one = 5
number_two = 3

print("Are number_one and number_two equal?", number_one == number_two)  # Equal to
print(
    "Are number_one and number_two not equal?", number_one != number_two
)  # Not equal to
print("Is number_one greater than number_two?", number_one > number_two)  # Greater than
print("Is number_one less than number_two?", number_one < number_two)  # Less than
print("Is 5 greater than or equal to 5?", 5 >= 5)  # Greater than or equal to
print(
    "Is number_one less than or equal to number_two?", number_one <= number_two
)  # Less than or equal to


# Logical Operators

print("Result of True and False:", True and False)
print("Result of True or False:", True or False)
print("Result of not True:", not True)


# Assignment Operators

number_one = 10
number_two = 5

result_number = number_one
print("Initial value of result_number:", result_number)

result_number += number_one  # Equivalent to result_number = result_number + number_one
print("After addition assignment:", result_number)

result_number -= number_one  # Equivalent to result_number = result_number - number_one
print("After subtraction assignment:", result_number)

result_number *= number_one  # Equivalent to result_number = result_number * number_one
print("After multiplication assignment:", result_number)

result_number /= number_one  # Equivalent to result_number = result_number / number_one
print("After division assignment:", result_number)

result_number %= number_one  # Equivalent to result_number = result_number % number_one
print("After modulus assignment:", result_number)

result_number **= (
    number_one  # Equivalent to result_number = result_number ** number_one
)
print("After exponentiation assignment:", result_number)

result_number //= (
    number_one  # Equivalent to result_number = result_number // number_one
)
print("After floor division assignment:", result_number)
