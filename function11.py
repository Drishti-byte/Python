#program to print all the subsets of a set 
def subset(nums, index = 0, current = None):
    if current is None:
        current = [] 
    if index == len(nums):
        print(current) 
        return 
    subset(nums, index + 1, current + [nums[index]]) 
    subset(nums, index + 1, current) 
nums = [1, 2, 3] 
print("All possible subsets are as follows:")
subset(nums)