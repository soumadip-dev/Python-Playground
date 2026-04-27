# Dunder Methods (Magic Methods) in Python
# Dunder methods are special methods that start and end with double underscores (__).
# They provide special behavior and are automatically called by Python in specific situations.


class Employee:

    # Constructor method
    # The __init__ method is automatically called when a new object is created.
    # It initializes the attributes of the object.
    def __init__(self, employee_name, employee_salary):
        self.employee_name = employee_name
        self.employee_salary = employee_salary

    # String representation for users
    # The __str__ method returns a readable string representation of the object.
    # It is called when we use print(object) or str(object).
    def __str__(self):
        return f"Employee Name: {self.employee_name}, Salary: {self.employee_salary}"

    # Official representation for developers
    # The __repr__ method returns a detailed representation of the object.
    # It is mainly used for debugging and is called by repr(object).
    def __repr__(self):
        return f"Employee('{self.employee_name}', {self.employee_salary})"

    # The __len__ method defines the behavior of the len() function for the object.
    # In this example, it returns the length of the employee's name.
    def __len__(self):
        return len(self.employee_name)


# Creating an Employee object
employee_one = Employee("John Doe", 34000)

# Accessing an attribute of the object
print("Employee salary:", employee_one.employee_salary)

# Calling the __str__ method
print(str(employee_one))

# Calling the __repr__ method
print(repr(employee_one))

# Calling the __len__ method
print("Length of employee name:", len(employee_one))


# Example of operator overloading using dunder methods
class Vector:

    # Constructor to initialize vector coordinates
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Overloading the + operator
    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    # Overloading the - operator
    def __sub__(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    # Overloading the * operator
    def __mul__(self, other_vector):
        return Vector(self.x * other_vector.x, self.y * other_vector.y)

    # String representation of the vector
    def __str__(self):
        return f"({self.x}, {self.y})"


# Creating two vector objects
vector_one = Vector(2, 3)
vector_two = Vector(4, 5)

# Adding the two vectors using operator overloading
result_vector = vector_one + vector_two  # Calls the __add__ method

# Printing the result vector
print("Result of vector addition:", result_vector)

# Printing one vector object
print("Vector one:", vector_one)
