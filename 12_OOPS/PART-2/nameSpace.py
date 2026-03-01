# Class and Object Namespace in Python


class Student:

    # Class attribute
    # This attribute belongs to the class and is shared by all objects of the class.
    origin_country = "India"


# Accessing the class attribute using the class name
print(f"Value from Student class: {Student.origin_country}")


# Adding another class attribute dynamically
Student.is_active = True

print(f"Value from Student class: {Student.is_active}")


# Creating an object (instance) of the Student class
first_student = Student()

# Accessing class attributes using the object
print(f"Value from first_student object: {first_student.origin_country}")
print(f"Value from first_student object: {first_student.is_active}")


# Creating object-specific attributes
first_student.is_active = (
    False  # This overrides the class attribute for this object only
)
first_student.favorite_flavor = "Vanilla"


# Printing the modified object attributes
print(
    f"Value of is_active for first_student after modification: {first_student.is_active}"
)
print(f"Favorite flavor of first_student: {first_student.favorite_flavor}")


# The class attribute remains unchanged
print(f"Value of is_active in Student class: {Student.is_active}")


# Accessing favorite_flavor using the class would cause an error
# because this attribute was added only to the object, not to the class.

# print(Student.favorite_flavor)  # This will raise an AttributeError
