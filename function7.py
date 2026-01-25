#program to print the greatest number 
def greatest(a, b, c):
    if a > b and b > c:
        return c 
    elif b > c and b > a:
        return b 
    else:
        return c 
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:")) 
res = greatest(a, b, c)
print("The greatest number is",res)