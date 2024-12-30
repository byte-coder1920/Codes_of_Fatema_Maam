#object
class Student:
  roll=''
  gpa=''
  def display(self):
    print(f"Name:{self.name},Roll:{self.roll},GPA:{self.gpa}")

r= Student()
r.name='rahin'
r.roll=2
r.gpa=3.00
r.display()

