#program to list the prime numbers in a given range
start = int(input("Enter the starting range:"))
end = int(input("Enter the ending range:")) 

for num in range(start,end + 1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num,"is prime") 