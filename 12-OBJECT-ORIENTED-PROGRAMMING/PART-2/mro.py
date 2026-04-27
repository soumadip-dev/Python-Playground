# Method Resolution Order (MRO) in Python
# MRO defines the order in which Python searches for attributes and methods in a class hierarchy.


class A:
    # Base class
    label = "A: Base Class"


class B(A):
    # Derived from class A
    label = "B: Derived Class"


class C(A):
    # Derived from class A
    label = "C: Derived Class"


class D(B, C):
    # Class D inherits from B first, then C
    pass


# Creating an object of class D
derived_object = D()

# Accessing the label attribute
# Python checks in this order according to MRO: D → B → C → A
print(derived_object.label)
