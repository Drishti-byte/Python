#program to find the sum of the series: x + x^2/2! + x^3/3!+ ........ + x^n/n!
x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))

fact = 1
sum = 0 
for i in range(1,n+1):
    sum += (x ** i) / i 
    fact *= i 
    if i < n:
        print(x,"^",i,"/",fact,"!","+") 
    else:
        print(x,"^",n,"/",fact,"!")
print("Sum = ",sum)