# Classes and Objects in Python

# Class:
# A class is a blueprint used to create objects.
# It defines the properties (attributes) and behaviors (methods) that the objects will have.
# Example: An exam form template that contains fields such as name, age, subjects, and father's name.

# Object:
# An object is an instance created from a class.
# It represents a real entity created using the class template.
# Example: A completed exam form containing the details of a specific student.


class Employee:
    # Class attribute (shared by all objects of this class)
    company_name = "Google"

    def get_salary(self):
        # 'self' represents the current object that calls this method.
        # Every method inside a class must include 'self' as the first parameter.

        salary_amount = 34000
        return salary_amount


# Creating the first object of the Employee class
first_employee = Employee()
print("Salary of the first employee:", first_employee.get_salary())


# Creating the second object of the Employee class
second_employee = Employee()
print("Salary of the second employee:", second_employee.get_salary())
