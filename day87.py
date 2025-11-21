#program to use default and paramterised constructor 
class Employee:
    def __init__(self, n, desig, salary): #Paramterised Constructor
        self.name = n 
        self.designation = desig 
        self.sal = salary 
    def displayDetails(self):
        print("Employee name:", self.name)
        print("Employee's Designation:", self.designation)
        print("Employee's Salary:", self.sal)
class Manager:
    def __init__(self):
        print("This is a default constructor with no parameter")
e = Employee("Meena", "HR", 100000)
e.displayDetails()
m = Manager() 