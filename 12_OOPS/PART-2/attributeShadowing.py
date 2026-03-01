# Attribute Shadowing in Python


# Class definition
class Student:
    # Class attributes (shared by all students)
    school_name = "ABC Public School"
    grade = "A"


# Creating a student object
student_one = Student()

# Accessing the class attribute through the object
print("Initial grade:", student_one.grade)

# Attribute shadowing:
# When we assign a value to the same attribute name in the object,
# it overrides (shadows) the class attribute for that object only.
student_one.grade = "B"

print(f"Grade from object after change: {student_one.grade}")
print(f"Grade from class remains unchanged: {Student.grade}")

# Deleting the object attribute
# After deletion, Python falls back to the class attribute
del student_one.grade

print(f"Grade after deleting object attribute: {student_one.grade}")

# Creating an attribute that does not exist in the class
student_one.nickname = "Sam"

# Deleting that object-specific attribute
del student_one.nickname

# print(student_one.nickname)
# This will raise an AttributeError because the attribute
# does not exist in either the object or the Student class.
