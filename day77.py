#program to check if a number is strong number or not (sum of factorial of the digits)
def factorial(num):
    if num == 1:
        return 1 
    else: 
        return num * factorial(num - 1) 
    
def strongNum(num):
    sum = 0
    while num != 0:
        d = num % 10 
        strNum = factorial(d)  
        sum += strNum 
        num = num // 10
    return sum
        
num = int(input("Enter a number:"))
res = strongNum(num)
if num == res: 
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")