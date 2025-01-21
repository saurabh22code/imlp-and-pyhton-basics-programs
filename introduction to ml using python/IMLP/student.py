#make a class object to display the student details

class student:
    def __init__(self,name,course,roll,marks):
        self.name=name #display the names
        self.course=course #dispaly the course
        self.roll=roll #diaplay the roll
        self.marks=marks #diaply the marks
        
    def student_details(self):
        print("Student details:")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Roll: {self.roll}")
        print(f"Marks: {self.marks}")
x=student("saurabh kumar","B.TECH CSE",25,99)
x.student_details()

       
        