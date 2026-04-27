# map(), filter(), and reduce() in Python


# ---------------------------
# map()
# ---------------------------
# The map() function applies a given function to every element in an iterable
# and returns a map object containing the transformed values.

numbers_list = [1, 2, 3, 4, 5]


# Function to calculate the square of a number
def calculate_square(number):
    return number * number


# Convert the map object into a list to display all results
squared_numbers_list = list(map(calculate_square, numbers_list))
print("Squared numbers:", squared_numbers_list)


# If we do not convert it to a list, map() returns an iterator.
# We can access the values by iterating through it.

squared_numbers_iterator = map(calculate_square, numbers_list)

print("Squared numbers using iteration:")
for squared_number in squared_numbers_iterator:
    print(squared_number)


# Using map() with a lambda function
numbers_multiplied_by_two = list(map(lambda number: number * 2, numbers_list))
print("Numbers multiplied by 2:", numbers_multiplied_by_two)


# ---------------------------
# filter()
# ---------------------------
# The filter() function selects elements from an iterable
# that satisfy a specific condition.

numbers_list = [3, 7, 10, 12, 4, 15]


# Function to check whether a number is greater than 9
def is_greater_than_nine(number):
    return number > 9


# Apply filter() to get numbers greater than 9
numbers_greater_than_nine = list(filter(is_greater_than_nine, numbers_list))
print("Numbers greater than 9:", numbers_greater_than_nine)


# Using filter() with a lambda function
numbers_greater_than_two = list(filter(lambda number: number > 2, numbers_list))
print("Numbers greater than 2:", numbers_greater_than_two)


# ---------------------------
# reduce()
# ---------------------------
# The reduce() function repeatedly applies a function to elements
# of an iterable until a single result remains.
# reduce() must be imported from the functools module.

from functools import reduce

numbers_list = [1, 2, 3, 4, 5, 6]


# Calculate the sum of numbers using a normal loop
total_sum = 0
for number in numbers_list:
    total_sum = total_sum + number

print("Sum calculated using a loop:", total_sum)


# Function used by reduce() to add two numbers
def add_numbers(first_number, second_number):
    return first_number + second_number


# Calculate the sum using reduce()
sum_using_reduce = reduce(add_numbers, numbers_list)


# Explanation of how reduce() works:
# numbers_list = [1, 2, 3, 4, 5, 6]
# Step 1: 1 + 2 = 3
# Step 2: 3 + 3 = 6
# Step 3: 6 + 4 = 10
# Step 4: 10 + 5 = 15
# Step 5: 15 + 6 = 21

print("Sum calculated using reduce():", sum_using_reduce)
