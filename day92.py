#program to implement operator overloading 
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y 
    def __str__(self):
        return (f"(x = {self.x}, y = {self.y})")
    def __add__(self, other):
        x = self.x + other.x 
        y = self.y + self.y 
        return Point(x, y)
    def __sub__(self, other):
        x = other.x - self.x 
        y = other.y - self.y 
        return Point(x, y)
    def __mul__(self, other):
        x = self.x * other.x 
        y = self.y * other.y 
        return Point(x, y)
    def __truediv__(self, other):
        x = self.x / other.x 
        y = self.y / other.y 
        return Point(x, y)
    def __floordiv__(self, other):
        x = self.x // other.x 
        y = self.y // other.y 
        return Point(x, y)
    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y 
        return Point(x, y)
p1 = Point(21, 67)
p2 = Point(45, 75)
print("First Point:", p1)
print("Second Point:", p2)
print("Sum:", p1 + p2)
print("Difference:", p1 - p2)
print("Product:", p1 * p2)
print("Quotient:", p1 / p2)
print("Quotient:", p1 // p2)
print("Remainder:", p1 % p2)