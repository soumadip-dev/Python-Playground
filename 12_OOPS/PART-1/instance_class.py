# Class Attributes and Instance Attributes in Python


class Employee:
    # Class attribute (shared by all objects of the class)
    default_bond_duration = 4

    def __init__(self, salary_amount, employee_name, bond_duration):
        # Instance attributes belong to a specific object
        self.employee_name = employee_name
        self.salary_amount = salary_amount

        # This instance attribute overrides the class attribute
        self.bond_duration = bond_duration


# Creating an object of the Employee class
employee_example = Employee(34000, "John Doe", 1)

# Instance attributes take priority over class attributes
print("Bond duration of the employee:", employee_example.bond_duration)
# Output: 1 (because the instance attribute overrides the class attribute value of 4)


class Student:
    # Class attribute (shared by all student objects)
    standard = 3

    def __init__(self, student_name, student_age):
        # Instance attributes specific to each student object
        self.student_name = student_name
        self.student_age = student_age


# Creating an object of the Student class
student_example = Student("Mohit Agarwal", 23)

# Since 'standard' is not defined as an instance attribute,
# Python uses the class attribute value
print("Student standard:", student_example.standard)

# We can also access the class attribute directly using the class name
# because it belongs to the class itself
print("Student standard from class:", Student.standard)


# Object Introspection:
# The dir() function returns a list of all attributes and methods
# available for the given object.
print("Attributes and methods available in student_example:", dir(student_example))
