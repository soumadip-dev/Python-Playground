# Operator Overloading in Python


# This class represents a point in a 2D coordinate system.
class Point:

    # Constructor to initialize the x and y coordinates of the point
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Method to add two Point objects without using operator overloading
    def add_points(self, other_point):
        # Add the x and y coordinates of both points
        new_x_coordinate = self.x + other_point.x
        new_y_coordinate = self.y + other_point.y

        # Return a new Point object with the resulting coordinates
        return Point(new_x_coordinate, new_y_coordinate)

    # Operator overloading for the + operator
    # This method allows two Point objects to be added using the + symbol
    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)


# Creating the first point object
first_point = Point(3, 2)

# Creating the second point object
second_point = Point(4, 5)

# Adding the two points using the normal method
result_point = first_point.add_points(second_point)

# Printing the coordinates of the resulting point
print("Result using method:", result_point.x, result_point.y)


# Adding the two points using operator overloading
# The + operator internally calls the __add__ method
result_point = first_point + second_point

print("Result using + operator:", result_point.x, result_point.y)


# Common operator overloading methods in Python

# __add__      → Overloads the + operator
# __sub__      → Overloads the - operator
# __mul__      → Overloads the * operator
# __truediv__  → Overloads the / operator
# __eq__       → Checks if two objects are equal
# __ne__       → Checks if two objects are not equal
# __lt__       → Checks if the first object is less than the second
# __le__       → Checks if the first object is less than or equal to the second
# __gt__       → Checks if the first object is greater than the second
# __ge__       → Checks if the first object is greater than or equal to the second
# __len__      → Returns the length of an object
# __getitem__  → Allows indexing access (e.g., object[index])
# __setitem__  → Allows modifying values using indexing
