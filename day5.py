#program to find roots of quadratic equation 
import math 
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
d = (b * b) - 4 * a * c 

if d < 0:
    print("No real roots are there")
elif d == 0:
    r1 = r2 = -b / (2 * a)
    print("Roots of the quadratic eq are:",r1,"and",r2) 
else:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots of the quadratic eq are:",r1,"and",r2)