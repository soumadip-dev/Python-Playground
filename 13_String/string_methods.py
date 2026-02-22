# STRING METHODS IN PYTHON

# Strings in Python are immutable.
# This means the characters inside a string cannot be changed
# after the string has been created.

full_name = "Soumadip Majila"

# Example (this will produce an error):
# full_name[0] = "R"
# Error: TypeError - 'str' object does not support item assignment


# LENGTH OF A STRING

# The len() function returns the total number of characters in a string.
name_length = len(full_name)
print(name_length)


# COMMON STRING METHODS

print(full_name.upper())  # Converts all characters to uppercase
print(full_name.lower())  # Converts all characters to lowercase
print(full_name.capitalize())  # Capitalizes only the first character of the string
print(full_name.title())  # Capitalizes the first letter of each word

# The original string remains unchanged because strings are immutable.
print(full_name)


# REMOVING EXTRA SPACES

text_with_extra_spaces = " Hello world "

# strip() removes spaces from both the beginning and the end
print(text_with_extra_spaces.strip())

# lstrip() removes spaces from the left side
print(text_with_extra_spaces.lstrip())

# rstrip() removes spaces from the right side
print(text_with_extra_spaces.rstrip())


# OTHER USEFUL STRING METHODS

sentence = "Python is fun and too much fun"

# find() returns the index of the first occurrence of a substring
print(sentence.find("is"))

# replace() replaces a substring with another substring
print(sentence.replace("fun", "awesome"))


# SPLIT AND JOIN METHODS

fruit_text = "Apples, bananas, pineapples"

# split() divides the string using the given separator and returns a list
fruit_list = fruit_text.split(", ")
print(fruit_list)

# join() combines list elements into a single string using a separator
joined_fruit_text = ", ".join(["Apples", "Bananas", "Pineapples"])
print(joined_fruit_text)


# STRING CHECKING METHODS

sample_text = "Python123"

# isalpha() returns True if all characters are letters
print(sample_text.isalpha())

# isdigit() returns True if all characters are digits
print(sample_text.isdigit())

# isalnum() returns True if all characters are letters or digits
print(sample_text.isalnum())

# isspace() returns True if the string contains only whitespace
print(sample_text.isspace())
