#program to print the grade of the student as per the percentage of marks 
per = float(input("Enter your percentage marks:"))
if per >= 90:
    print("Your grade is A") 
elif per >= 80 and per < 90:
    print("Your grade is B")
elif per >= 60 and per < 80:
    print("Your grade is C")
elif per >= 50 and per < 60:
    print("Your grade is D")
else: 
    print("Your grade is E")