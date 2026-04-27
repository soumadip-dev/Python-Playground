try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    print(
        "Select the operation you want to perform:\n"
        "Press + for addition\n"
        "Press - for subtraction\n"
        "Press * for multiplication\n"
        "Press / for division"
    )

    selected_operation = input("Enter the operation: ")

    match selected_operation:
        case "+":
            print(
                f"The result of {first_number} + {second_number} is {first_number + second_number}"
            )

        case "-":
            print(
                f"The result of {first_number} - {second_number} is {first_number - second_number}"
            )

        case "*":
            print(
                f"The result of {first_number} * {second_number} is {first_number * second_number}"
            )

        case "/":
            if second_number == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(
                    f"The result of {first_number} / {second_number} is {first_number / second_number}"
                )

        case _:
            print("Invalid operation selected.")

# Handle invalid input (non-integer values)
except ValueError:
    print("Invalid input. Please enter numeric values for both numbers.")

# Handle any unexpected errors
except Exception:
    print("An unexpected error occurred.")
