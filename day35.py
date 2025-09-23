#program to perform binary search 
arr = [11, 23, 39, 44, 52, 67, 79, 83, 99, 101]
target = int(input("Enter the number you want to search:"))
start = 0
end = len(arr) - 1
while start <= end: 
    mid = (start + end) // 2 
    if arr[mid] == target:
        print(target,"found at position",mid+1)
        break
    elif target > arr[mid]:
        start = mid + 1
    elif target < arr[mid]:
        end = mid - 1
else:
    print(target,"not found")