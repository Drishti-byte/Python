#program to search and update a dictionary 
def createDict(demp, n):
    for i in range(n):
        ename = input("Enter the name of the employee:") 
        sal = int(input("Enter the salary of the employee:"))
        demp.update({ename : sal}) 

def search(demp, name):
    if name in demp:
        print("Current salary:", demp[name])
        demp[name] += demp[name] * 0.25
        print("Salary updated !!!!")
    else:
        print("Employee name not found !!!!")

demp = {} 
n = int(input("How many employees are there:"))
createDict(demp, n) 
name = input("Enter employee's name to increase their salary:") 
search(demp, name) 
print("Dictionary:", demp)

#program to store friend's names and their phone numbers 
# def createDict(dfr, n):
#     for i in range(n):
#         name = input("Enter name:")
#         phonenum = int(input("Enter phone number:")) 
#         dfr.update({name : phonenum}) 

# def search(dfr, name):
#     if name in dfr:
#         print("Phone Number:", dfr[name]) 
#     else:
#         print("Friend name not found in the dictionary !!!") 

# dfr = {}
# n = int(input("Enter how many friends do you have:"))
# createDict(dfr, n) 
# print("Dictionary:", dfr)
# name = input("Enter friend name to search their contact details:") 
# search(dfr, name) 
# print("Dictionary:", dfr)