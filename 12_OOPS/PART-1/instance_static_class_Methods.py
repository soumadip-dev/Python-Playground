# Instance Method, Static Method, and Class Method in Python
# All examples are related to a person.


# ---------------------------
# Instance Method Example
# ---------------------------


class Person:
    # Constructor to initialize the person's name, age, and city
    def __init__(self, person_name, person_age, city_name):
        self.person_name = person_name
        self.person_age = person_age
        self.city_name = city_name

    # Instance method
    # This method uses the data stored in the object
    def get_person_details(self):
        return (
            f"Name: {self.person_name}, Age: {self.person_age}, City: {self.city_name}"
        )


# Creating a person object
first_person = Person("Soumadip", 23, "Durgapur")

# Calling the instance method
print(first_person.get_person_details())


# ---------------------------
# Static Method Example
# ---------------------------

# Sometimes a function is related to a class but does not use
# any object data. In that case, we use a static method.


class PersonTextUtility:

    # Static method to clean and split a list of hobbies
    @staticmethod
    def split_hobbies(hobby_text):
        return [hobby.strip() for hobby in hobby_text.split(",")]


# Raw hobby list entered by a user
raw_hobbies = "reading, coding, gaming"

# Static method can be called using the class name
print(PersonTextUtility.split_hobbies(raw_hobbies))


# ---------------------------
# Class Method Example
# ---------------------------


class PersonProfile:
    # Constructor to initialize name, age, and profession
    def __init__(self, person_name, person_age, profession):
        self.person_name = person_name
        self.person_age = person_age
        self.profession = profession

    # Class method to create an object from a dictionary
    @classmethod
    def from_dictionary(cls, person_data):
        # cls refers to the PersonProfile class
        return cls(
            person_data["person_name"],
            person_data["person_age"],
            person_data["profession"],
        )


# Creating an object using the class method
person = PersonProfile.from_dictionary(
    {"person_name": "Rahul", "person_age": 25, "profession": "Software Developer"}
)

print(person.person_name, person.person_age, person.profession)
