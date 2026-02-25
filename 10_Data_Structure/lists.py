# Lists in Python

# A list is an ordered and mutable (changeable) collection of items.
# It allows multiple values to be stored in a single variable.

marks_list = [54, 23, 64, 93, 32]

# A list can also store elements of different data types.
mixed_data_list = [10, "Hello", 3.14, False]

print("Marks list:", marks_list)
print("Mixed data list:", mixed_data_list)


# Accessing elements using an index (index starts from 0)
print("Second element in marks_list:", marks_list[1])
print("Third element in mixed_data_list:", mixed_data_list[2])


# Slicing a list (retrieving a range of elements)
print("Elements from index 2 to 3:", marks_list[2:4])


# List Methods
# Most list methods modify the original list.

# Add an element to the end of the list
marks_list.append(36)
print("After appending 36:", marks_list)


# Remove the last element from the list
marks_list.pop()
print("After removing the last element:", marks_list)


# Extend the list by adding elements from another list
additional_marks_list = [1, 3, 4, 5, 6]
marks_list.extend(additional_marks_list)

print("After extending with another list:", marks_list)


# Insert an element at a specific index
marks_list.insert(1, 99)
print("After inserting 99 at index 1:", marks_list)


# Reverse the order of the list
marks_list.reverse()
print("After reversing the list:", marks_list)


# Sort the list in ascending order
marks_list.sort()
print("After sorting the list:", marks_list)


# List Comprehension
# An efficient way to create a new list from an existing iterable.

# This creates a list containing the squares of numbers from 0 to 4
squared_numbers_list = [number**2 for number in range(5)]

print("Squared numbers list:", squared_numbers_list)
