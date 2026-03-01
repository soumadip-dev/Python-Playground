# Constructor in Python

# A constructor is a special method that is automatically called
# when an object of a class is created. In Python, the constructor
# method is named __init__.


class Employee:

    # The constructor initializes the attributes of the object
    def __init__(self, job_role, company_name):
        # Assign the values passed during object creation
        self.job_role = job_role
        self.company_name = company_name

    # Method to describe the employee
    def describe_employee(self):
        return f"This employee works at {self.company_name} as a {self.job_role}."


# Creating the first employee object
first_employee = Employee("Developer", "Google")
print(first_employee.describe_employee())


# Creating the second employee object
second_employee = Employee("Designer", "Infosys")
print(second_employee.describe_employee())



