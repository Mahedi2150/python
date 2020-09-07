class student:
    roll=""
    cgpa=""
    def setValue(self,roll,cgpa):
        self.roll=roll
        self.cgpa=cgpa
    def display(self):
        print(f"Roll = {self.roll} CGPA = {self.cgpa}")

rahim=student()
rahim.setValue(101,3.50)
rahim.display()

karim=student()
karim.setValue(102,3.75)
karim.display()
