#program to allot the grades based on marks 
marks = int(input("Enter your marks:"))
if(marks >= 90):
    print("Your grade is A")
elif(marks >= 80 and marks < 90):
    print("Your grade is B")
elif(marks >= 70 and marks < 80):
    print("Your grade is C")
else:
    print("Your grade is D")