# -----------------------------------
# IF–ELSE CONDITIONAL STATEMENTS
# -----------------------------------

"""
1. Write a program that asks the user for a number and determines
whether the number is positive, negative, or zero.
"""

user_number = int(input("Enter a number: "))

if user_number > 0:
    print("The number is positive.")
elif user_number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


"""
2. Create a program that checks whether a person is eligible to vote.
A person is eligible if their age is 18 or older.
"""

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


"""
3. Write a program that takes a number from the user and checks whether
the number is even or odd.
"""

number_to_check = int(input("Enter a number: "))

if number_to_check % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# -----------------------------------
# MATCH–CASE STATEMENTS
# -----------------------------------

"""
1. Ask the user to enter a day number (1–7) and print the corresponding
day of the week using a match-case statement.
"""

day_number = int(input("Enter a day number (1–7): "))

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number.")


"""
2. Write a program using match-case that simulates a simple calculator.
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation_symbol = input("Enter an operation (+, -, *, /): ")

match operation_symbol:
    case "+":
        result = first_number + second_number
        print("Result:", result)

    case "-":
        result = first_number - second_number
        print("Result:", result)

    case "*":
        result = first_number * second_number
        print("Result:", result)

    case "/":
        if second_number != 0:
            result = first_number / second_number
            print("Result:", result)
        else:
            print("Division by zero is not allowed.")

    case _:
        print("Invalid operation.")


# -----------------------------------
# FOR LOOPS
# -----------------------------------

"""
1. Print numbers from 1 to 10 using a for loop.
"""

for number in range(1, 11):
    print(number)


"""
2. Print the multiplication table of a number entered by the user.
"""

table_number = int(input("Enter a number to display its multiplication table: "))

for multiplier in range(1, 11):
    product = table_number * multiplier
    print(table_number, "x", multiplier, "=", product)


"""
3. Calculate the sum of all numbers from 1 to 100.
"""

total_sum = 0

for number in range(1, 101):
    total_sum += number

print("The sum of numbers from 1 to 100 is:", total_sum)


"""
4. Print the following star pattern:

*
**
***
****
"""

for row in range(1, 5):
    print("*" * row)


# -----------------------------------
# WHILE LOOPS
# -----------------------------------

"""
1. Print numbers from 1 to 10 using a while loop.
"""

current_number = 1

while current_number <= 10:
    print(current_number)
    current_number += 1


"""
2. Write a program that keeps asking the user to enter a password
until they enter the correct one.
"""

correct_password = "abc123"
entered_password = input("Enter the password: ")

while entered_password != correct_password:
    print("Incorrect password. Please try again.")
    entered_password = input("Enter the password: ")

print("Access granted.")


"""
3. Use a while loop to reverse a given number.
Example: 123 → 321
"""

original_number = 123
reversed_number = 0

while original_number > 0:
    last_digit = original_number % 10
    reversed_number = reversed_number * 10 + last_digit
    original_number = original_number // 10

print("Reversed number:", reversed_number)
