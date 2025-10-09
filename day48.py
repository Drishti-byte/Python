#program to find the cartesian product of two lists 
a = eval(input("Enter a list of numbers:")) 
b = eval(input("Enter another list of numbers:")) 
res = [] 
for num1 in a:
    for num2 in b:
        res.append((num1, num2)) 
print("Cartesian Product of list 1 and list 2 is:",res) 