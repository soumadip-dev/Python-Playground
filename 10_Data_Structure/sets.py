# Sets in Python

# A set is an unordered collection of unique elements.
# Duplicate values are automatically removed.

numbers_set = {3, 23, 2, 11, 2}
# The value 2 appears only once because sets do not allow duplicate elements.

print("Set elements:", numbers_set)
print("Data type of numbers_set:", type(numbers_set))


# Sets do not support indexing because they are unordered collections.
# Example (this would cause an error):
# print(numbers_set[1])


# Set Methods

# Add an element to the set
numbers_set.add(5)
print("After adding 5:", numbers_set)


# Remove a specific element from the set
numbers_set.remove(2)
print("After removing 2:", numbers_set)


# If we try to remove an element that does not exist in the set,
# the remove() method will raise an error.

# numbers_set.remove(100)  # This would raise a KeyError.


# To avoid this error, we can use discard().
# discard() does nothing if the element is not found.

numbers_set.discard(10)
print("After discarding 10 (if present):", numbers_set)


# pop() removes and returns a random element from the set
numbers_set.pop()
print("After removing a random element:", numbers_set)


# Set Operations

set_a = {1, 2, 3}
set_b = {3, 4, 5}


# Union of two sets
# The union (A ∪ B) includes all elements that are in set_a, set_b, or both.

union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)  # {1, 2, 3, 4, 5}


# Intersection of two sets
# The intersection (A ∩ B) includes only the elements common to both sets.

intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)  # {3}


# Difference of two sets
# The difference (A - B) includes elements that are in set_a but not in set_b.

difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)  # {1, 2}
