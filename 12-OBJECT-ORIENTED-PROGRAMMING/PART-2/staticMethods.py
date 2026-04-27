# Static Method Example in Python


# Example where creating an object is unnecessary
class TextProcessor:

    # This method removes extra spaces and splits a shopping list into individual items
    def split_items(self, text):
        return [item.strip() for item in text.split(",")]


# Raw shopping list entered by a user
raw_items = "rice  , milk, bread"

# Here we must create an object to call the method
processor = TextProcessor()

print(processor.split_items(raw_items))
# In this case, creating an object is unnecessary because the method
# does not use any instance data.


# Solution: Use a static method
class TextUtility:

    # Static method does not require an object or class instance
    @staticmethod
    def split_items(text):
        return [item.strip() for item in text.split(",")]


# Now we can call the method directly using the class name
print(TextUtility.split_items(raw_items))
