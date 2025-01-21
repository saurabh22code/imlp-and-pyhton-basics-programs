class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}'s age is {self.age}"
        
p1=student("Saurabh Agarwal",25)
print(p1)
