"""
1. Create a list fruits = ["apple", "banana", "cherry"].
   i. Print the first fruit.
   ii. Replace "banana" with "orange".
   iii. Print the length of the list.
"""

fruits = ["apple", "banana", "cherry"]

print("First fruit:", fruits[0])

fruits[1] = "orange"
print("Updated list after replacing 'banana' with 'orange':", fruits)

print("Length of the list:", len(fruits))


"""
2. Create a list of numbers from 1 to 10.
   i. Print the first three numbers using slicing.
   ii. Print the last three numbers using slicing.
"""

numbers_list = [number for number in range(1, 11)]

print("First three numbers:", numbers_list[:3])
print("Last three numbers:", numbers_list[-3:])


"""
3. Start with numbers = [5, 2, 9, 1, 7] and perform the following operations:
   i. Sort the list in ascending order.
   ii. Append the number 10 to the list.
   iii. Remove the number 2 from the list.
"""

numbers = [5, 2, 9, 1, 7]

numbers.sort()
print("Sorted list in ascending order:", numbers)

numbers.append(10)
print("List after appending 10:", numbers)

numbers.remove(2)
print("List after removing 2:", numbers)


"""
4. Create a list names = ["Alice", "Bob", "Charlie"] and insert "David"
   at index 1 using the insert() method.
"""

names = ["Alice", "Bob", "Charlie"]

print("Original list:", names)

names.insert(1, "David")
print("Updated list after inserting 'David' at index 1:", names)


"""
5. Create a tuple coordinates = (10, 20) and print both elements.
"""

coordinates = (10, 20)

print("First element of the tuple:", coordinates[0])
print("Second element of the tuple:", coordinates[1])


"""
6. Try to modify the tuple by setting coordinates[0] = 50.
   This will raise an error because tuples are immutable.
"""

# coordinates[0] = 50
# TypeError: 'tuple' object does not support item assignment


"""
7. Convert the tuple to a list, modify the first element to 50,
   and convert it back to a tuple.
"""

sample_tuple = (10, 20, 30)

print("Original tuple:", sample_tuple)

sample_list = list(sample_tuple)
print("Tuple converted to list:", sample_list)

sample_list[0] = 50
print("List after modifying the first element:", sample_list)

sample_tuple = tuple(sample_list)
print("List converted back to tuple:", sample_tuple)


"""
8. Create a set my_set = {1, 2, 3, 3, 4} and print it.
   Duplicate elements are automatically removed in a set.
"""

my_set = {1, 2, 3, 3, 4}

print("Set after removing duplicates:", my_set)


"""
9. Add 5 to the set, remove 2, and check whether 4 exists in the set.
"""

my_set.add(5)
print("Set after adding 5:", my_set)

my_set.discard(2)
print("Set after removing 2:", my_set)

print("Is 4 present in the set?", 4 in my_set)


"""
10. Create two sets:
    a = {1, 2, 3}
    b = {3, 4, 5}

    Find:
    i. Union
    ii. Intersection
    iii. Difference (a - b)
"""

set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

difference_set = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference_set)


"""
11. Create a dictionary:
student = {"name": "John", "age": 20, "grade": "A"}

Perform the following:
i. Print the value of "name".
ii. Change "grade" to "A+".
iii. Add a new key "city" with value "Delhi".
"""

student = {"name": "John", "age": 20, "grade": "A"}

print("Student name:", student["name"])

student["grade"] = "A+"
print("Dictionary after updating grade:", student)

student["city"] = "Delhi"
print("Dictionary after adding city:", student)


"""
12. Create a dictionary of three friends and their phone numbers.
Use:
i. keys() to get all names
ii. values() to get all numbers
iii. items() to loop through key-value pairs
"""

friends_phone_numbers = {
    "John": 1234567890,
    "Alice": 9876543210,
    "Bob": 1122334455,
}

print("Friend names:", friends_phone_numbers.keys())
print("Phone numbers:", friends_phone_numbers.values())

for name, phone_number in friends_phone_numbers.items():
    print("Phone number of", name, "is", phone_number)


"""
13. Remove duplicate numbers from a list using a set.
"""

numbers_with_duplicates = [1, 2, 1, 4, 5, 5, 6, 7, 8, 8, 5, 4, 1]

print("Original list:", numbers_with_duplicates)

unique_numbers = set(numbers_with_duplicates)
print("List after removing duplicates:", unique_numbers)


"""
14. Given a dictionary of products and their prices,
find the product with the highest price.
"""

products = {"apple": 10, "banana": 20, "orange": 30}

highest_price = max(products.values())

print("Highest product price:", highest_price)


"""
15. Merge two dictionaries into one.
"""

dictionary_one = {"a": 1, "b": 2, "c": 3}
dictionary_two = {"d": 4, "e": 5, "f": 6}

merged_dictionary = {**dictionary_one, **dictionary_two}

print("Merged dictionary:", merged_dictionary)
