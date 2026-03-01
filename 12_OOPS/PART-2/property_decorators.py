# Property Decorators in Python


# This class represents an animal in a zoo
class Animal:
    # Constructor to initialize the age of the animal
    def __init__(self, age):
        self._age = age  # _age is a private attribute

    # Getter method for age using @property
    # This allows controlled access to the age attribute
    @property
    def age(self):
        # Example logic: returning age + 1 (e.g., next year age)
        return self._age + 1

    # Setter method for age using @age.setter
    # This allows controlled modification of the age attribute
    @age.setter
    def age(self, age):
        if age < 0:
            # Raise an error if the age is negative
            raise ValueError("Age cannot be negative")
        self._age = age


# Creating an Animal object
zebra = Animal(2)

# Accessing age via the getter
print("Age of zebra:", zebra.age)  # Output will be 3 (2 + 1)

# Modifying age via the setter
zebra.age = 5
print("Updated age of zebra:", zebra.age)  # Output will be 6 (5 + 1)

# Attempting to set a negative age raises an error
# zebra.age = -1  # Uncommenting this line will raise ValueError: Age cannot be negative
