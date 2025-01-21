"""1. Write a python program to create Car Class 
a. Constructor (_init_) to 
initialize object attributes like car maker , car model & manufacturing year
b.Method to display car details by Creating objects"""

# Define a class named 'Car'
class Car:
    # Constructor (_init_) to initialize object attributes
    def __init__(self, make, model, year):
        self.make = make        # Attribute for car make
        self.model = model      # Attribute for car model
        self.year = year        # Attribute for car manufacturing year

    # Method to display car details
    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

    # Method to simulate driving the car
    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is now driving!")

# Creating objects (instances of the class)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing object methods and attributes
car1.display_details()  # Displays car1 details
car1.drive()            # Simulates driving car1

car2.display_details()  # Displays car2 details
car2.drive()            # Simulates driving car2