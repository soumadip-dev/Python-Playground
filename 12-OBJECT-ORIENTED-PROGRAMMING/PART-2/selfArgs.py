# self argument in Python


class Employee:
    # Class attribute shared by all employees
    company_name = "Google"

    def describe_employee(self):
        # This method returns a sentence describing where the employee works.
        # 'self' refers to the object that calls this method.
        # It allows the method to access attributes of that specific object.

        return f"This employee works at {self.company_name}."


# Creating the first employee object
first_employee = Employee()

# Calling the method using the object (recommended way)
print(first_employee.describe_employee())


# Calling the method using the class directly
# This will raise an error because Python does not automatically
# know which object should be passed as the 'self' argument.

# print(Employee.describe_employee())  # This would raise a TypeError


# Correct way when calling through the class:
# We must manually pass the object as the first argument.
print(Employee.describe_employee(first_employee))


# Creating another employee object
second_employee = Employee()

# Overriding the company_name for this specific object
second_employee.company_name = "Infosys"

# This demonstrates attribute shadowing
print(second_employee.describe_employee())
