# Inheritance in Python
# ---------------------


# Parent Class (Superclass)
# The Animal class defines common properties and behaviors
# that all animals share.
class Animal:

    # Constructor to initialize the animal's name and its sound
    def __init__(self, animal_name, animal_sound):
        self.animal_name = animal_name
        self.animal_sound = animal_sound

    # Method to describe the sound made by the animal
    def make_sound(self):
        print(f"The {self.animal_name} makes the sound '{self.animal_sound}'.")


# Child Class (Subclass)
# The Dog class inherits attributes and methods from Animal
# and also defines its own specific behavior.
class Dog(Animal):

    # Method specific to Dog
    def guard_house(self):
        print("The dog is guarding the house.")


# Creating an object of the Dog class
pet_dog = Dog("Dog", "Bark")

# Calling the inherited method from the Animal class
pet_dog.make_sound()

# Calling the method defined in the Dog class
pet_dog.guard_house()


# Composition in Python
# ---------------------
# Composition means one class contains an object of another class
# and uses its functionality.


class PetShop:

    # Constructor creates an Animal object inside the PetShop class
    def __init__(self):
        # The shop keeps a pet animal available
        self.shop_pet = Animal("Cat", "Meow")

    # Method to display the pet available in the shop
    def show_available_pet(self):
        print(
            f"The shop has a {self.shop_pet.animal_name} that makes the sound '{self.shop_pet.animal_sound}'."
        )

    # Method that uses the Animal class method
    def demonstrate_pet_sound(self):
        self.shop_pet.make_sound()


# Creating an object of the PetShop class
pet_shop = PetShop()

# Using the composed Animal object
pet_shop.show_available_pet()

# Calling the Animal method through composition
pet_shop.demonstrate_pet_sound()
