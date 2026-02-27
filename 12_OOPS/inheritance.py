# Inheritance in Python

# Parent Class (Superclass)
# The Animal class defines common attributes and behaviors that all animals share.


class Animal:

    # Class attribute shared by all objects of this class
    country = "Australia"

    def __init__(self, animal_name):
        # Constructor method used to initialize the object's attributes
        self.animal_name = animal_name

    def speak(self):
        # This method describes the sound made by an animal
        print(f"{self.animal_name} makes a sound.")

    def run(self):
        # This method describes the running behavior of an animal
        print(f"{self.animal_name} runs quickly.")


# Child Class (Subclass)
# The Dog class inherits attributes and methods from the Animal class.


class Dog(Animal):

    def __init__(self, animal_name, breed_name):
        # super() is used to call the constructor of the parent class
        # It allows the child class to reuse the initialization logic of the parent class
        super().__init__(animal_name)

        # Additional attribute specific to the Dog class
        self.breed_name = breed_name

    def speak(self):
        # This method overrides the speak() method from the parent class
        # This concept is called Method Overriding
        print(f"{self.animal_name} barks: Woof!")

    def show_breed(self):
        # This method displays the breed of the dog
        print(f"{self.animal_name} belongs to the {self.breed_name} breed.")


# Creating an object of the Animal class
animal_object = Animal("Unknown Animal")
animal_object.speak()


# Creating an object of the Dog class
dog_object = Dog("Bruno", "Labrador")

dog_object.speak()  # Calls the overridden method in Dog
dog_object.run()  # Inherited method from Animal
dog_object.show_breed()  # Method defined in Dog class


# Accessing the class attribute inherited from the parent class
print("Country attribute from the parent class:", dog_object.country)
