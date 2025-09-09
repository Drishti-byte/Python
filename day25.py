#program to list the armstrong numbers
for num in range(100,1000):
    a = num 
    sum = 0 
    while a > 0:
        d = a % 10 
        sum = sum + d ** 3 
        a = a // 10 
    if sum == num:
        print(num,"is armstrong number")