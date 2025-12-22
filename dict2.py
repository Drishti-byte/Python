#program to store marks of student in a dictionary
subject = {}
s1 = int(input("Enter marks in physics:"))
subject.update({"physics": s1})
s2 = int(input("Enter marks in maths:"))
subject.update({"maths": s2})
s3 = int(input("Enter marks in chemistry:"))
subject.update({"chemistry": s3})
print(subject)