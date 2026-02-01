#program to find the highest scorer in the given list
student = [{"name" : "Asha", "marks" : 85}, {"name" : "Rahul", "marks" : 92}, {"name" : "Zara", "marks" : 78}, {"name" : "Vikram", "marks" : 90}]
def topper(student):
    t = student[0] 
    for stu in student: 
        if stu["marks"] > t["marks"]:
            t = stu 
    return t 
top = topper(student) 
print("Name:", top["name"])
print("Marks:", top["marks"])