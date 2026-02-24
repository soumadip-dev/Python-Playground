# STRING SLICING IN PYTHON

student_name = "Soumadip"

# Positive index slicing
# Syntax: string[start : end]
# Slicing starts from the 'start' index and stops at (end - 1).

print(student_name[0:3])  # Characters from index 0 to 2 → "Sou"


# Negative index slicing
# Negative indexing starts from the end of the string.

print(
    student_name[2:-1]
)  # Characters from index 2 to the second-last character → "umadi"


# If the starting index is omitted, Python assumes it is 0
print(student_name[:4])  # Characters from index 0 to 3 → "Soum"

# If the ending index is omitted, Python slices until the end of the string
print(student_name[1:])  # Characters from index 1 to the last character → "oumadip"

# SLICING WITH STEP

# Syntax: string[start : end : step]
# The step value determines how many characters Python moves forward each time.
# If step = 2, Python selects every second character (skips one character each time).

print(student_name[0:8:2])  # Every second character → "Smai"
print(student_name[1:8:2])  # Every second character starting from index 1 → "uai"
