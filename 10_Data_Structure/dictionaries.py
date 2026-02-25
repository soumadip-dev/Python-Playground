# Dictionaries in Python

# A dictionary stores data in key-value pairs.
# It allows fast lookup of values using keys.

student_details = {"name": "Alice", "age": 21, "grade": "A"}

print("Student details:", student_details)
print("Data type of student_details:", type(student_details))


# Accessing values using keys
print("Student name:", student_details["name"])
print("Student age:", student_details["age"])


# Dictionary Methods

# Print all keys in the dictionary
print("Keys:", student_details.keys())

# Print all values in the dictionary
print("Values:", student_details.values())

# Print all key-value pairs
print("Items:", student_details.items())


# Remove the 'age' key from the dictionary
student_details.pop("age")
print("Dictionary after removing 'age':", student_details)


# Remove all items from the dictionary
student_details.clear()
print("Dictionary after clearing all items:", student_details)


# Dictionary Comprehension
# Create a dictionary where keys are numbers and values are their squares

squares_dictionary = {number: number**2 for number in range(5)}

print("Squares dictionary:", squares_dictionary)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
