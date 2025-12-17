#program to check whether the student has pass or failed in the exam 
m1 = int(input("Enter your marks in the first subject:"))
m2 = int(input("Enter your marks in the second subject:"))
m3 = int(input("Enter your marks in the third subject:"))
m4 = int(input("Enter your marks in the fourth subject:"))
m5 = int(input("Enter your marks in the fifth subject:"))

total = m1 + m2 + m3 + m4 + m5
avg = total / 5 
print("Total marks obtained:",total)
print("Average marks obtained:",avg)
if avg >= 90:
    print("Your grade is A")
elif avg >= 80 and avg < 90:
    print("Your grade is B")
elif avg >= 70 and avg < 80:
    print("Your grade is C")
elif avg >= 60 and avg < 70:
    print("Your grade is D")
else:
    print("Your grade is E")