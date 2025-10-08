#program to find the union and intersection of two lists 
list1 = eval(input("Enter a list of numbers:")) 
list2 = eval(input("Enter another list of numbers:")) 
uni = list1.copy() 
inter = [] 
for val in list2:
    if val in uni: 
        inter.append(val) 
    else: 
        uni.append(val) 
print("List 1:",list1) 
print("List 2:",list2) 
print("Union of list 1 and list 2:",uni) 
print("Intersection of list 1 and list 2:",inter) 

#finding complement of a list
# Universal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# list1 = eval(input("Enter a list of numbers:")) 
# comp1 = [] 
# for val in Universal:
#     if val not in list1:
#         comp1.append(val) 
# print("List 1:",list1) 
# print("Universal set:",Universal) 
# print("Complement of list 1:",comp1) 