#class
class Student:
    name = ''
    roll = ''
    gpa = ''

    def setvalue(self, name, roll, gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, GPA: {self.gpa}")

# Create an instance of Student and set values
r = Student()
r.setvalue('karim', 2, 3.55)
r.display()

# Create another instance of Student
r = Student()
print(isinstance(r, Student))

# Set values directly
r.name = 'rahin'
r.roll = 2
r.gpa = 3.00

# Display the values
print(f"Name: {r.name}, Roll: {r.roll}, GPA: {r.gpa}")