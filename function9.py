#program to maximum of N numbers
def maximum(*numbers):
    return max(numbers) 

n = int(input("How many numbers are there:")) 
nums = [] 
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num) 
print("Highest number is:", maximum(*nums)) 