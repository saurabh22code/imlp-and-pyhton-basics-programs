class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id=employee_id #attribute for employee ID
        self.name=name #attribute for name
        self.position=position #attribute for pssition
        self.salary=salary #attribute for salary
        
    def display_details(self):
        print("Employee Details:") 
        print(f"Employee ID: {self.employee_id}")  
        print(f"Name: {self.name}")     
        print(f"Position: {self.position}") 
        print(f"Salary: {self.salary}")
    
    def annual_salary(self):
        print("employee anual salary:")
        return self.salary*12
        
    
    def apply_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"New salary after {percentage}% raise: ${self.salary:.2f}")
        
    
        
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