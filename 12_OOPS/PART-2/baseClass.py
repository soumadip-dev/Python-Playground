# Ways to Access a Base Class (Parent Class)


# Parent class
class Employee:
    # Constructor to initialize employee name and base salary
    def __init__(self, employee_name, base_salary):
        self.employee_name = employee_name
        self.base_salary = base_salary


# Example of repeating code (not recommended)
# Here we manually assign the same attributes instead of reusing the parent constructor
class Manager(Employee):
    def __init__(self, employee_name, base_salary, team_size):
        self.employee_name = employee_name
        self.base_salary = base_salary
        self.team_size = team_size


# Better approach: Explicitly calling the parent class constructor
class Developer(Employee):
    def __init__(self, employee_name, base_salary, programming_language):
        # Explicit call to the parent class constructor
        Employee.__init__(self, employee_name, base_salary)
        self.programming_language = programming_language


# Best approach: Using super() to call the parent class constructor
class DataScientist(Employee):
    def __init__(self, employee_name, base_salary, specialization):
        # Implicit call to the parent class constructor using super()
        super().__init__(employee_name, base_salary)
        self.specialization = specialization
