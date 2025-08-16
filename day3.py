#program to input the name, marks(5 sub), total, per 
fullname = input("Enter your name: ")
m1 = int(input("Enter your marks in eng subject: "))
m2 = int(input("Enter your marks in hindi subject: "))
m3 = int(input("Enter your marks in maths subject: "))
m4 = int(input("Enter your marks in science subject: "))
m5 = int(input("Enter your marks in s.st subject: "))
total = m1 + m2 + m3 + m4 + m5 
per = total / 5
print("---------------------------------------------------------------")
print("Report Card of:",fullname)
print("Total marks scored:",total)
print("Percentage obtained:",per,"%")
if(per >= 40):
    print("Congratulations !!!! You are promoted to class 11th")
else:
    print("Sorry!! You have to reappear")
print("---------------------------------------------------------------")