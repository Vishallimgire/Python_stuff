class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades or []

    def add_marks(self, marks):
        self.grades.append(marks)
    
student = Student('vishal',[])
student1 = Student('mahesh',[0])
student.add_marks(90)
print(student.grades)
print(student1.grades)