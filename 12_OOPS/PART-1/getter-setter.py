# Getter and Setter Methods in Python


class Employee:

    # Constructor to initialize the employee's full name and salary
    def __init__(self, full_name, salary_amount):
        self._full_name = full_name  # Protected attribute
        self._salary = salary_amount  # Protected attribute

    # Getter method
    # The @property decorator allows this method to be accessed like an attribute
    @property
    def first_name(self):
        # Extract and return the first name from the full name
        name_parts = self._full_name.split(" ")
        return name_parts[0]

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter method for salary
    # Allows controlled modification of the salary
    @salary.setter
    def salary(self, new_salary_amount):

        # Validate the new salary value
        if new_salary_amount < 0:
            raise ValueError("Salary cannot be negative.")

        if new_salary_amount < self._salary:
            raise ValueError("Salary cannot be reduced.")

        # Update the salary if validation passes
        self._salary = new_salary_amount


# Creating an Employee object
first_employee = Employee("John Doe", 50000)

# Accessing the first name using the getter property
print("Employee first name:", first_employee.first_name)

# Updating the salary using the setter
first_employee.salary = 60000

# first_employee.salary = 10000  # This will raise a ValueError

# Printing the updated salary
print("Updated salary:", first_employee.salary)
