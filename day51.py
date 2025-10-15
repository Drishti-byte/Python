#program to create a dictionary for employees 
def createdict(demp, n):
    for i in range(n):
        ename = input("Enter name of the employee:")
        sal = int(input("Enter the salary of the employee:")) 
        jobTitle = input("Enter the job:")
        demp.update({ename : [sal, jobTitle]}) 

demp = {}
n = int(input("How many employees are there:")) 
createdict(demp, n)
print("Dictionary:", demp)

#program to create a dictionary for countries and capitals 
# def createDict(dcoun, n):
#     for i in range(n):
#         country = input("Enter the country:")
#         capital = input("Enter the capital:")
#         dcoun.update({country : capital}) 

# dcoun = {}
# n = int(input("Enter the number of countries you want to enter:"))
# createDict(dcoun, n)
# print("Dictionary:", dcoun) 