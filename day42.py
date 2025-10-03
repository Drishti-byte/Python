#program to implement bubble sort 
list = eval(input("Enter a list of numbers:"))
n = len(list)
print("Before sorting:",list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j] 
print("After sorting:",list)