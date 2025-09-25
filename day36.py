#program to reverse a list
list = [23, 34, 56, 78, 90]
n = len(list)
print("Before reversing, the elements are:")
print(list)
for i in range(n // 2):
    list[i], list[n - i - 1] = list[n - i- 1], list[i]
print("After reversing, the elements are:")
print(list)