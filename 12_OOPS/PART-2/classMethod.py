# Class Methods in Python


# This class represents an animal in a zoo
class Animal:
    # Constructor to initialize species, age, and habitat
    def __init__(self, species, age, habitat):
        self.species = species
        self.age = age
        self.habitat = habitat

    # Class method to create an object from a dictionary  
    @classmethod
    def from_dict(cls, animal_data):
        # cls refers to the Animal class
        return cls(animal_data["species"], animal_data["age"], animal_data["habitat"])

    # Class method to create an object from a string
    @classmethod
    def from_string(cls, animal_string):
        # Split the string by comma and unpack values
        species, age, habitat = animal_string.split(",")
        return cls(species, age, habitat)


# Creating animal objects using different methods

# Using the normal constructor
animal1 = Animal("Lion", "5", "Savannah")

# Using class method from_dict
animal2 = Animal.from_dict({"species": "Elephant", "age": "10", "habitat": "Forest"})

# Using class method from_string
animal3 = Animal.from_string("Giraffe,7,Savannah")

# Printing animal details
print(
    f"The animal created using the normal constructor is a {animal1.species}, aged {animal1.age} years, living in the {animal1.habitat}."
)
print(
    f"The animal created using the class method `from_dict` is a {animal2.species}, aged {animal2.age} years, living in the {animal2.habitat}."
)
print(
    f"The animal created using the class method `from_string` is a {animal3.species}, aged {animal3.age} years, living in the {animal3.habitat}."
)
