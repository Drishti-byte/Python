#program to implement single level inheritance 
class Shape:
    def __init__(self, s):
        self.side = s
    def area(self):
        area = self.side * self.side 
        print("Area of square:", area, "sq cm") 
class Rectangle(Shape):
    def __init__(self, l, b):
        self.length = l 
        self.breadth = b 
    def area(self):
        area = self.length * self.breadth 
        print("Area of rectangle:", area, "sq cm")
r = Rectangle(29, 87)
r.area()