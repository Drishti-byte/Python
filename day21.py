#program to print the sum of the series 1 + 1/2 + 1/3 + ............. + 1/n 
n = int(input("Enter a number:")) 
sum = 0

for i in range(1,n + 1):
    if i < n:
        print("1/",i,"+")
    else:
        print("1/",i)
    sum += 1/i 
print("Sum = 1/",round(sum,2))