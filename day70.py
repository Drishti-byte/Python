#program to find the sum of digits using recursion 
def sumOfDigits(num): 
    if num % 10 == 0:
        return num 
    else:
        d = num % 10
        return d + sumOfDigits(num // 10) 

n = int(input("Enter a number:"))
res = sumOfDigits(n) 
print("Sum of digits of",n,"is",res)