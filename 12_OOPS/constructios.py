# Constructor in Python Classes


class Employee:
    # The constructor method is automatically called when an object is created.
    # It is used to initialize the attributes of the object.

    def __init__(self, salary_amount, employee_name, bond_duration):
        # Assigning values to the object's attributes
        self.employee_name = employee_name
        self.salary_amount = salary_amount
        self.bond_duration = bond_duration

    def get_employee_details(self):
        # This method returns the details of the employee
        return f"The employee name is {self.employee_name}, the salary is {self.salary_amount}, and the bond duration is {self.bond_duration} year(s)."


# Creating an object of the Employee class
first_employee = Employee(34000, "John Doe", 1)

# Printing the employee details
print(first_employee.get_employee_details())
