#program to find second highest value in a list 
list = [12, 23, 90, 45, 67, 98, 78]
m = list[0] 
s = 0 
for num in list:
    if num > m:
        m = num 
for num in list:
    if num != m and num > s:
        s = num 
print("The highest value in the list is:",m)
print("The second highest value in the list is:",s)