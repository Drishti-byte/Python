#program to implement multi-level inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self, name, age, sno, marks):
        super().__init__(name, age)
        self.sno = sno 
        self.marks = marks 
    def show(self):
        super().show()
        print("Student roll no:", self.sno)
        print("Student Marks:", self.marks)
class StudentCouncil(Student):
    def __init__(self, name, age, sno, marks, scdob):
        super().__init__(name, age, sno, marks)
        self.dob = scdob 
    def show(self):
        super().show()
        print("Student dob:", self.dob)
p = Person("Kanishka", 15)
p.show()
print()
s = Student("Kanishka", 15, 120, 95)
s.show()
print()
sc = StudentCouncil("Kanishka", 15, 120, 95, "23-07-2006")
sc.show()