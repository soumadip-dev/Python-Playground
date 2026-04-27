# STRINGS IN PYTHON
# A string can be created using single quotes, double quotes, or triple quotes.

person_name = "Soumadip"
print(person_name)

# Triple single quotes can also store a string
full_name = '''Soumadip Majila'''
print(full_name)

# Triple double quotes allow multi-line strings
description = """Ram
is a
good
boy
"""
print(description)



# STRING INDEXING

student_name = "Ram"

# Index positions
# Positive indexing:  0   1   2
#                     R   a   m

# Negative indexing: -3  -2  -1
#                     R   a   m

print(student_name[0])   # First character
print(student_name[1])   # Second character
print(student_name[-1])  # Last character
print(student_name[-3])  # First character using negative index

# print(student_name[8])  
# This will produce an error: IndexError (string index out of range)