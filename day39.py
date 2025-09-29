#program to remove duplicates from the list
list = eval(input("Enter a list of values:"))
print("Before removing duplicates:",list)
i = 0
while i < len(list):
    if list.count(list[i]) > 1:
        list.remove(list[i])
    else:
        i += 1
print("After removing duplicates:",list)