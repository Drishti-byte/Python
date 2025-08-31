#program to find the lcm of two numbers 
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a 
    else:
        return gcd(b, a % b) 

g = gcd(n1, n2) 
lcm = (n1 * n2) / g 
print("LCM of",n1,"and",n2,"is",lcm)