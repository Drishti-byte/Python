#program to create a binary file 
import pickle 
f = open("student.dat", "ab") 
n = int(input("How many students you want to add:"))
for i in range(n):
    sid = int(input("Enter student's roll no:")) 
    sname = input("Enter student's name:")
    marks = int(input("Enter marks:")) 
    stu = [sid, sname, marks]
    pickle.dump(stu, f) 
f.close()
print("Data entered successfully!!!")
print("Please check student.dat file in your directory")