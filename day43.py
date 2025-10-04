#program to implement insertion sort 
list = eval(input("Enter a list of numbers:")) 
n = len(list) 
print("Before sorting:",list) 
for i in range(1, n):
    num = list[i] 
    j = i - 1 
    while(num < list[j] and j >= 0):
        list[j + 1] = list[j] 
        j = j - 1 
    list[j + 1] = num 
print("After sorting:",list) 