# Comments, Escape Sequences, and Print Statement in Python

print("Hello, how are you?")

# Single-line comments:
# Arjun, please complete this code.
# Rohan, please review the code.


# Multi-line comment:
"""
This is an example
of a multi-line comment.
"""


# Escape Sequences:
# Escape sequences are used to include special characters inside strings.

print("Hello, how are you?\nI am doing well.")      # \n → New line
print("SampleText\tAnotherText")                   # \t → Tab space
print("SampleText \\ AnotherText")                 # \\ → Backslash
print("SampleText \"Quoted Text\"")                # \" → Double quote
print("SampleText 'Single Quote'")                 # Single quote inside double quotes


# Print statement examples

print("Hello World", "Soumadip", sep=" - ", end=" ~ ")
# By default, sep = " " (space) and end = "\n" (new line).
# We can override them using the sep and end parameters.

print("This text appears after the tilde.")