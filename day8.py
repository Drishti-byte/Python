#program to check whether the triangle is equilateral, isosceles, scalene triangle 
a = int(input("Enter the length of a:"))
b = int(input("Enter the length of b:"))
c = int(input("Enter the length of c:")) 
if a == b  and b == c:
    print("It is an equilateral triangle")
elif a == b or b == c or c == a:
    print("It is a isosceles triangle")
else:
    print("It is a scalene triangle")