#program to print the series: x + x^2 + x^3 + ........... + x^n
x = int(input("Enter the value of x:")) 
n = int(input("Enter the value of n:")) 

sum = 0
for i in range(1,n + 1):
    if i < n:
        print(x,"^",i,"+")
    else:
        print(x,"^",i)
    sum += x ** i 
print("Sum:",sum)