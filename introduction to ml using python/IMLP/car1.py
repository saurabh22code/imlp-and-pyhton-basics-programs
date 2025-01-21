class Car:
    def __init__(self,car_maker,car_model,year):
        self.car_maker=car_maker #attribute for an car make 
        self.car_model=car_model #attribute for an car model
        self.year=year #attribute for an car manufactorer year
        
    def car_details(self):
        print("Car details:")
        print(f"Car_Maker: {self.car_maker}")
        print(f"Car_model: {self.car_model}")
        print(f"year: {self.year}")
        
    def driving(self):
        print(f"The {self.year} {self.car_maker} {self.car_model} is now driving")

carw=Car("Toyota","Fortuner",2006)
carw.car_details()
carw.driving()