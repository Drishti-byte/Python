#program to print the sum of the digits of a number 
num = int(input("Enter a number:")) 
sum = 0 
n = num 
while num != 0:
    dig = num % 10 
    sum = sum + dig 
    num = num // 10 
print("The sum of",n,"is",sum)