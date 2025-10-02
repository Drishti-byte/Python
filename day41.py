#program to implement selection sort 
list = [12, 45, 78, 90, 56, 34, 10, 5] 
print("Before sorting:",list) 
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print("After sorting:",list)