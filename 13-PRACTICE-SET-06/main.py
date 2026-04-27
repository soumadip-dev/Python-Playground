"""
Create a class Car with a method drive().
Create an object of the Car class and call drive() to print a message.
"""


class Car:

    # This method prints a message indicating that the car is moving
    def drive(self):
        print("The car is moving.")


# Creating an object of the Car class
bmw_car = Car()

# Calling the drive() method
bmw_car.drive()

"""
Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
Create an object and print the person's name and age.
"""


class Person:

    # Constructor to initialize the name and age of a person
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age


# Creating an object of the Person class
employee_person = Person("Soumadip", 21)

# Printing the person's details
print("Name:", employee_person.name)
print("Age:", employee_person.age)


"""
Create a base class Animal with a method sound() that prints "Some sound".
Create a derived class Dog that overrides the sound() method.
Create an object of Dog and call sound() to print "Bark!".
"""


class Animal:

    # This method prints a general animal sound
    def sound(self):
        print("Some sound")


class Dog(Animal):

    # This method overrides the sound() method from the Animal class
    def sound(self):
        print("Bark!")


# Creating an object of the Dog class
husky_dog = Dog()

# Calling the overridden method
husky_dog.sound()
