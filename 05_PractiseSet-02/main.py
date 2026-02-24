# -----------------------------------
# IF–ELSE CONDITIONAL STATEMENTS
# -----------------------------------

"""
Program 1:
Ask the user to enter a number and determine
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
Program 2:
Check whether a person is eligible to vote.
A person is eligible if their age is 18 or older.
"""

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


"""
Program 3:
Ask the user for a number and check whether
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
Program 4:
Ask the user to enter a number (1–7) and display
the corresponding day of the week.
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
Program 5:
Create a simple calculator using match-case.
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
Program 6:
Print numbers from 1 to 10 using a for loop.
"""

for number in range(1, 11):
    print(number)


"""
Program 7:
Print the multiplication table of a number entered by the user.
"""

table_number = int(input("Enter a number to display its multiplication table: "))

for multiplier in range(1, 11):
    product = table_number * multiplier
    print(table_number, "x", multiplier, "=", product)


"""
Program 8:
Calculate the sum of numbers from 1 to 100.
"""

total_sum = 0

for number in range(1, 101):
    total_sum += number

print("The sum of numbers from 1 to 100 is:", total_sum)


"""
Program 9:
Print the following star pattern:

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
Program 10:
Print numbers from 1 to 10 using a while loop.
"""

current_number = 1

while current_number <= 10:
    print(current_number)
    current_number += 1


"""
Program 11:
Keep asking the user for a password until the correct password is entered.
"""

correct_password = "abc123"
entered_password = input("Enter the password: ")

while entered_password != correct_password:
    print("Incorrect password. Please try again.")
    entered_password = input("Enter the password: ")

print("Access granted.")


"""
Program 12:
Reverse a number using a while loop.
Example: 123 → 321
"""

original_number = 123
reversed_number = 0

while original_number > 0:
    last_digit = original_number % 10
    reversed_number = reversed_number * 10 + last_digit
    original_number = original_number // 10

print("Reversed number:", reversed_number)


# -----------------------------------
# BREAK, CONTINUE, AND PASS
# -----------------------------------

"""
Program 13:
Print numbers from 1 to 10, but stop the loop
when the number becomes 7.
"""

for number in range(1, 11):
    print(number)
    if number == 7:
        break


"""
Program 14:
Print numbers from 1 to 10 but skip the number 5.
"""

for number in range(1, 11):
    if number == 5:
        continue
    print(number)


"""
Program 15:
Loop through numbers from 1 to 5.
Do nothing when the number is 3.
"""

for number in range(1, 6):
    if number == 3:
        pass
    print(number)
