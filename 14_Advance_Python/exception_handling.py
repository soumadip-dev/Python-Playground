# Exception Handling in Python

# Limit the number of attempts a user can make
attempt_count = 0
maximum_attempts = 2

while attempt_count < maximum_attempts:
    try:
        # Take input from the user
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))

        # Perform division
        division_result = first_number / second_number

        print(
            f"The result of dividing {first_number} by {second_number} is {division_result}"
        )

        # Increase the attempt counter after a successful operation
        attempt_count += 1

    except ZeroDivisionError:
        # This error occurs when the user tries to divide by zero
        print("Error: Division by zero is not allowed.")

    except ValueError:
        # This error occurs when the user enters a non-numeric value
        print("Error: Please enter valid integer numbers.")

    except Exception as error:
        # This block handles any other unexpected exception
        print(f"An unexpected error occurred: {error}")


# Handling multiple exceptions using a tuple
try:
    user_number = int(input("Enter a number: "))
    division_result = 10 / user_number

except (ValueError, ZeroDivisionError) as error:
    # Handles both invalid input and division by zero
    print(f"Error occurred: {error}")

except Exception as error:
    # Handles any other unexpected error
    print(f"An unexpected error occurred: {error}")


# Using else and finally blocks
# else runs only if no exception occurs
# finally runs whether an exception occurs or not

division_result = None  # Define the variable before the try block

try:
    user_number = int(input("Enter a number: "))
    division_result = 10 / user_number

except Exception as error:
    print(f"An unexpected error occurred: {error}")

else:
    # This block executes only if no exception occurs
    print("Division was successful.")
    print(f"Result: {division_result}")

finally:
    # This block always runs
    print("The division operation has finished.")

    # Check if the result exists before printing
    if division_result is not None:
        print(f"Final result value: {division_result}")


# Raising exceptions using the 'raise' keyword
# We can manually raise exceptions to enforce rules in our program.


def check_user_age(user_age):
    # Validate that the user is at least 18 years old
    if user_age < 18:
        raise ValueError("Age must be 18 or older.")
    return "Access granted"


try:
    print(check_user_age(20))
    print(check_user_age(16))
except ValueError as error:
    print(f"Error: {error}")


# Custom Exceptions
# Python allows you to define your own custom exception classes by creating a new
# class that inherits from the built-in Exception class.


class InvalidAgeError(Exception):
    # Custom exception for invalid age
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)


def verify_user_age(age):
    # Check if the user meets the age requirement
    if age < 18:
        raise InvalidAgeError()
    return "Welcome!"


try:
    print(verify_user_age(16))
except InvalidAgeError as error:
    print(f"Error: {error}")
