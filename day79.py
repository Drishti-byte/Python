#program to shift the elements to the left 
def lShift(arr, n):
    for i in range(n):
        val = arr.pop(0) 
        arr.append(val) 
    print("After sorting:")
    print(arr)
arr = eval(input("Enter a list of elements:")) 
n = int(input("Enter the number of elements you want to shift to the left:"))
print("Before shifting:")
print(arr)
lShift(arr, n)