#create a class for student and show result 
class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno 
        self.name = name 
        self.marks = marks
    def displayDetails(self):
        print("Student Rollno:", self.rollno)
        print("Student Name:", self.name)
        print("Student Marks:", self.marks) 
    def result(self):
        if self.marks >= 40:
            print(self.name, "is pass")
        else:
            print(self.name, "has failed to clear the exam")
s = Student(101, "Shikha", 89) 
s.displayDetails()
s.result()