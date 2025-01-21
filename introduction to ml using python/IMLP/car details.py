class Car:
    def __init__(self,make,model,year,milage):
        self.make=make
        self.model=model
        self.year=year
        self.milage=milage
        
    def display_details(self):
        print(f"Car details:")
        print(f"make: {self.make}")
        print(f"model: {self.model}")
        print(f"year:{self.year}")
        print(f"Milage: {self.milage} Km/L")
        
    def car_age(self,current_year):
        car_age=current_year-self.year
        print("The car's age is",car_age,"years")
        
    def update_milage(self,new_milage):
        if new_milage>self.milage:
            self.milage=new_milage
            print(f"milage updated to :{self.milage} Km/L")
        else:
            print(f"error: new milage must be greater then the ")   


car1=Car("toyota","camey",2015,24)
car1.display_details()
current_year=2025
age=car1.car_age(current_year)
print(f"car age: {age} years") 
car1.update_milage(12)
car1.display_details()