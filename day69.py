#program to find HCF of two numbers using recursion 
def hcf(n1, n2):
    rem = n1 % n2 
    if rem == 0:
        return n2 
    else:
        return hcf(n2, rem) 

a = int(input("Enter first number:"))
b = int(input("Enter second number:")) 
res = hcf(a, b) 
print(f"HCF of {a} and {b} is {res}")