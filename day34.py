#program to implement linear search 
arr = [10, 28, 34, 45, 59, 65, 71, 82, 99, 100] 
target = int(input("Enter a number to be searched:")) 
for i in range(0, len(arr)):
    if arr[i] == target:
        print("Number found at position",(i+1))
        break 
else: 
    print("Number not found")