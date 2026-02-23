"""
1. Create a string variable containing your full name.
   i. Print the first character of the string.
   ii. Print the last character of the string.
   iii. Print the length of the string.
"""

full_name = "Soumadip Majila"

print("First character of the name:", full_name[0])
print("Last character of the name:", full_name[-1])
print("Length of the name:", len(full_name))


"""
2. Concatenate two strings "Hello" and "World" with a space between them.
"""

first_word = "Hello"
second_word = "World"

greeting_message = first_word + " " + second_word
print("Greeting message:", greeting_message)


"""
3. Given the string text = "Python Programming", perform the following:
   i. Print the first 6 characters.
   ii. Print the last 6 characters.
   iii. Print every second character from the string.
"""

text = "Python Programming"

print("First 6 characters:", text[:6])
print("Last 6 characters:", text[-6:])
print("Every second character:", text[::2])


"""
4. Reverse the string 'text' using slicing.
"""

reversed_text = text[::-1]
print("Reversed string:", reversed_text)


"""
5. Take the string " i love python programming " and:
   - Remove extra spaces from both ends.
   - Convert it to title case.
   - Count how many times the letter 'o' appears.
"""

sentence_with_spaces = " i love python programming "

trimmed_sentence = sentence_with_spaces.strip()
title_case_sentence = trimmed_sentence.title()

print("Sentence after removing extra spaces:", trimmed_sentence)
print("Sentence in title case:", title_case_sentence)

letter_to_count = "o"
occurrence_count = trimmed_sentence.count(letter_to_count)

print("The letter", letter_to_count, "appears", occurrence_count, "times.")


"""
6. Check if the string '123abc' is alphanumeric.
"""

test_string = "123abc"
print("Is the string alphanumeric?", test_string.isalnum())


"""
7. Using format(), create the sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.
"""

person_name = "John"
person_age = 25

formatted_sentence = "My name is {} and I am {} years old.".format(
    person_name, person_age
)
print(formatted_sentence)


"""
8. Create the same sentence using f-strings.
"""

f_string_sentence = f"My name is {person_name} and I am {person_age} years old."
print(f_string_sentence)


"""
9. Given the sentence "Coding in Python is fun",
replace the word "fun" with "awesome".
"""

sentence = "Coding in Python is fun"

updated_sentence = sentence.replace("fun", "awesome")
print("Updated sentence:", updated_sentence)


"""
10. Find the index of the word "Python" in the sentence.
"""

python_index = sentence.find("Python")
print("Index of the word 'Python':", python_index)


"""
11. Convert the entire sentence to uppercase and print it.
"""

uppercase_sentence = sentence.upper()
print("Sentence in uppercase:", uppercase_sentence)

"""
12. Write a program that counts how many vowels are in a given string.
"""

input_sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for character in input_sentence:
    if character in vowels:
        vowel_count += 1

print("Total number of vowels in the sentence:", vowel_count)

"""
13. Take a user input string and check if it is a palindrome
(same forwards and backwards).
"""

user_input_string = input("Enter a string to check for palindrome: ")

reversed_string = user_input_string[::-1]

if user_input_string == reversed_string:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
