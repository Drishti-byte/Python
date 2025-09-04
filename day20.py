#program to check whether the number is palindrome or not 
num = int(input("Enter a number:")) 
revNum = 0
n = num

while num != 0:
    dig = num % 10 
    revNum = (revNum * 10) + dig 
    num = num // 10 

if revNum == n:
    print(n,"is palindrome") 
else:
    print(n,"is not palindrome")