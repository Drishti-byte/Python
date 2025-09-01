#program to calculate Greatest Common Divisor(GCD) 
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

def gcd(a, b):
    if a == 0:
        return b 
    elif b == 0:
        return a 
    else:
        return gcd(b, a % b) 
    
res = gcd(n1, n2)
print("HCF of",n1,"and",n2,"is",res)