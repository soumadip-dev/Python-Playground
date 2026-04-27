# Walrus Operator (:=) in Python
# The walrus operator is an assignment expression operator.
# It allows assigning a value to a variable while evaluating an expression.


def slow_calculation():
    # This function simulates a time-consuming calculation.
    print("Processing step 1...")
    print("Processing step 2...")
    print("Processing step 3...")
    print("Processing step 4...")
    print("Processing step 5...")
    return 70


# Bad approach
# The function is called multiple times, which is inefficient.
print("Bad approach")

if slow_calculation() > 10:
    print(slow_calculation())
else:
    print("The result is not greater than 10")


# Slightly better approach
# The function result is stored in a variable and reused.
print("\nSlightly better approach")

result_value = slow_calculation()

if result_value > 10:
    print(result_value)
else:
    print("The result is not greater than 10")


# Best approach using the walrus operator
# The value is assigned and checked in the same expression.
print("\nBest approach using the walrus operator")

if (calculated_value := slow_calculation()) > 10:
    print(calculated_value)
else:
    print("The result is not greater than 10")


# Simple use case of the walrus operator
# The input value is assigned and checked in the loop condition.
print("\nSimple use case of the walrus operator")

while user_input := input("Enter a value (type 'q' to quit): "):
    if user_input == "q":
        print("Exiting the program.")
        break

    print("You entered:", user_input)
