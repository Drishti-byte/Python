#program to find factorial of a number using recursion 
num = int(input("Enter a number:")) 
def factorial(num):
    if num == 1:
        return 1 
    else:
        return num * factorial(num - 1)
print("The factorial of",num,"is",factorial(num))

#program to print numbers from 1 to 10 using recursion 
# def printNumber(num):
#     if num == 0:
#         return 0 
#     else:
#         print(num)
#         return printNumber(num - 1) 
# num = int(input("Enter a number:"))
# printNumber(num)