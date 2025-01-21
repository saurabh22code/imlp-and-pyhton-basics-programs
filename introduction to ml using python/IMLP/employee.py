"""2. Write a python program to create Employee Class 
a. Constructor (_init_) to 
initialize object attributes like employee_id , name , position, salary
b.Method to display employee details .

program : 
"""
class Employee:
    # Constructor to initialize employee details
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id  # Employee ID
        self.name = name                # Employee name
        self.position = position        # Employee position/job title
        self.salary = salary            # Employee salary

    # Method to display employee details
    def display_details(self):
        print("Employee Details:")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

    # Method to calculate annual salary
    def annual_salary(self):
        return self.salary * 12

    # Method to apply a salary raise
    def apply_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"New salary after {percentage}% raise: ${self.salary:.2f}")

# Main program execution
if __name__ == "__main__":
    # Creating an employee object
    emp1 = Employee(101, "John Doe", "Software Engineer", 5000)
    
    # Displaying employee details
    emp1.display_details()
    
    # Calculating and displaying annual salary
    print(f"Annual Salary: ${emp1.annual_salary()}")
    
    # Applying a salary raise of 10%
    emp1.apply_raise(10)
    
    # Display updated employee details after raise
    emp1.display_details()