class student:

    def __init__(self,roll,cgpa):
        self.roll=roll
        self.cgpa=cgpa
    def display(self):
        print(f"Roll = {self.roll} CGPA = {self.cgpa}")

rahim=student(101,3.50)
rahim.display()

karim=student(102,3.75)
karim.display()

