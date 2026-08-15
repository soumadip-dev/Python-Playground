from abc import ABC, abstractmethod


# Abstract class that defines the common structure for a bank application.
# It contains methods that every bank application should have.
class BankApp(ABC):

    def database(self):
        # This is a concrete method.
        # Child classes can directly use this method.
        print("Connected to database")

    @abstractmethod
    def security(self):
        # This is an abstract method.
        # Every child class must provide its own implementation
        # of the security method.
        pass


# MobileApp inherits from the abstract BankApp class.
class MobileApp(BankApp):

    def mobile_login(self):
        # This method is specific to the mobile application.
        print("Logged in to mobile app")

    def security(self):
        # Providing the required implementation of the
        # abstract security method.
        print("Mobile security enabled")


# Creating an object of the MobileApp class.
# This is possible because MobileApp has implemented
# the abstract security() method.
mobile_app = MobileApp()

# Calling the method specific to MobileApp.
mobile_app.mobile_login()

# Calling the concrete method inherited from BankApp.
mobile_app.database()

# Calling the implementation of the abstract method
# provided by MobileApp.
mobile_app.security()
