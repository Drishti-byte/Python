#program to calculate the hypotenuse of right angled triangle 
import math 
s = int(input("Enter side: "))
p = int(input("Enter perpendicular: "))
h = math.sqrt((s*s) + (p * p))
print("Hypotenuse of right angled triangle:",h)