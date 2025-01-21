class Employee:
    def __init__(self,name,employee_id,email,designation,salary):
        self.name=name
        self.employee_id=employee_id
        self.email=email
        self.designation=designation
        self.salary=salary
        
    def dispaly_details(self):
        print("The employee details are listed below:")
        print(f"Name: {self.name} \nEmployee ID: {self.employee_id} \nEmail ID: {self.email} \nDesignation: {self.designation} \nSalary: {self.salary}" )

    def anual_salary(self):
        print("Anual salary: ",self.salary*12)

    def increment(self,percentage):
        self.salary+=self.salary*(percentage/100)
        print(f"The new salary after increment is ${self.salary}")

x=Employee("Shailja mishra",112,"shailjamishra@gmail.com","software developer",200000)
x.dispaly_details()
x.anual_salary()
x.increment(10)   
