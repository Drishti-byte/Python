#program to print the fibonacci series (0, 1, 1, 2, 3, 5, 8.........) 
n = int(input("Enter the value of n:")) 

a = 0
b = 1 
print(a)
print(b)
for el in range(n+1):
    c = a + b 
    a = b 
    b = c 
    print(c)