#program to overload comparison operators 
class Rectangle:
    def __init__(self, l, b):
        self.l = l 
        self.b = b 
    def __str__(self):
        return f"Length = {self.l} and Breadth = {self.b}\n"
    def __gt__(self, other):
        if self.l * self.b > other.l * other.b:
            return True 
        else:
            return False 
r1 = Rectangle(10, 9)
r2 = Rectangle(17, 15)
print("First Rectangle:", r1)
print("Second Rectangle:", r2)
if r1 > r2:
    print("First rectangle is bigger in area") 
else:
    print("Second rectangle is bigger in area")