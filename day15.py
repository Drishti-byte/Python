#program to check whether the number is prime or not 
num = int(input("Enter a number:")) 
isPrime = True 

if num == 1:
    print("1 is not a prime number")  
elif num == 0:
    print("0 is neither prime nor composite")   
else:
    for el in range(2,num):
        if(num % el == 0):
            isPrime = False
            break 

    if isPrime == True:
        print(num,"is prime") 
    else:
        print(num,"is not prime")