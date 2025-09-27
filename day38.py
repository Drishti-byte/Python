#program to swap 1st half of the list with 2nd half 
list = [12, 23, 45, 50, 67, 79, 80]
print("Before swap: ",list)
n = len(list)
if n % 2 == 0:
    gap = n//2 
else:
    gap = n // 2 + 1 
for i in range(n // 2):
    list[i], list[i + gap] = list[i + gap], list[i]
print("After swap: ",list)