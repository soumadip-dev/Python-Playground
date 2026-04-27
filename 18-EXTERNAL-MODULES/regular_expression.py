# Regular Expressions (re module) in Python
# Regular expressions are used for pattern matching, searching, and text processing.

import re

text_content = "The quick brown fox jumps over the lazy dog."


# Search for a specific word in the text
search_result = re.search("brown", text_content)

if search_result:
    print("Match found.")
    print(f"Start index: {search_result.start()}")
    print(f"End index: {search_result.end()}")
else:
    print("No match found.")


# Find all occurrences of a word (case-insensitive search)
all_matches = re.findall("the", text_content, re.IGNORECASE)

print(f"Matches found: {all_matches}")
print(f"Total number of matches: {len(all_matches)}")


# Replace a word in the text
updated_text = re.sub("fox", "rabbit", text_content)

print(f"Updated text: {updated_text}")


# Useful website for testing regular expressions:
# https://regexr.com/
