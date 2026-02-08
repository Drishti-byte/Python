#program to create lists and perform operations on them
marks = [12.9,78.4,56.9,36.7,98.7]
print(marks)
print(type(marks))
student = ["Karan",95.4,17,"Delhi"] #Lists can store more than one data type & are mutable
print(student)
student[0] = "Arjun"
print(student)

#List slicing 
print(marks[1:4])
marks.append(17.8)
print(marks)
print(marks.sort())
print(marks)
print(marks.sort(reverse = True)) #reverse order
print(marks.reverse())
print(marks)
marks.insert(3,45)
print(marks)
list = [2,1,3,1]
list.pop(1)
print(list)