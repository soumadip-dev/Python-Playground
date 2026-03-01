# Classes and Objects Example


class Student:
    pass


# Checking the type of the class itself
print(type(Student))
# Output: <class 'type'>
# In Python, classes are also objects created by the built-in 'type' class.


# Creating an object of the Student class
first_student = Student()

# Checking the type of the object
print(type(first_student))
# Output: <class '__main__.Student'>


# Checking whether the object was created from the Student class
print(type(first_student) is Student)
# This expression returns True if the object belongs to the Student class.
