#program to create a dictionary
info = {
    "name" : "Drishti",
    "subject" : ["pyhton","C","Java"],
    "age" : 30,
    "marks" : 98.1,
    "is_adult" : True
}
print(info)
print(type(info))
info["surname"] = "Bansal"
print(info)

#Nested Dictionary
student = {
    "name" : "Drishti",
    "subjects" : {
        "phy" : 78,
        "chem" : 89,
        "maths" : 77
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["maths"])

#Methods in dictionary
print(student.keys())
print(list(student.keys()))  #Type casting to list
print(len(student))
print(student.values())
print(student.items())
print(student.get("name2"))
print(student["name2"])
student.update({"city" : "Delhi"})
print(student)