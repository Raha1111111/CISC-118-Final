#B
def __init__(self, name):
    # This is the constructor method for a Python class.
    # It's called when a new instance of the class is created.
    self.name = name  # This line sets the 'name' attribute of the class instance to the value passed as 'name' when the instance is created.

#C
class Person:
    def __init__(self, name):
        # Initialize the name attribute for each new instance of Person
        self.name = name

    def greet(self):
        # Simple method that prints a greeting message
        print(f"Hello, my name is {self.name}!")

#D
# Assuming Customer inherits from Person and possibly adds more features
class Customer(Person):
    def display_customer_info(self):
        # Simple method that prints customer information
        print(f"Customer Name: {self.name}")

# Create an instance of Customer
customer = Customer("John Doe")

# Set the attribute (although it's already set during initialization)
customer.name = "John Doe"

# Call the method from the Person class
customer.greet()

# Optionally, call the new method from Customer, if any
customer.display_customer_info()
