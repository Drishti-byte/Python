#program to rotate the list by n positions 
a = eval(input("Enter a list of numbers:")) 
n = int(input("Enter the number of positions you want to rotate:"))
print(a)
for i in range(n):              # a = a[n:] + a[:n]
    temp = a.pop(0)   
    a.append(temp)       
for i in range(n):
    temp = a[0]   
    for j in range(len(a) - 1):
        a[j] = a[j + 1] 
    a[-1] = temp 
print(a) 

#shifting from right 
# a = a[-n :] + a[: -n]
# for i in range(len(a) - n):
#     a.append(a[i])
# print(a) 