#program to swap adjacent numbers in the list
list = [12, 23, 45, 34, 78, 67, 56]
print("Before swapping, the elements of the list:")
print(list)
for i in range(0,len(list), 2):
    if i + 1 < len(list):
        list[i],list[i + 1] = list[i + 1],list[i]
print("After swapping, the elements of the list are:")
print(list)