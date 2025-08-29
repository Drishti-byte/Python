#program to check whether the number is a perfect number or not 
num = int(input("Enter a number:")) 
perfectNum = 0

if num == 0:
    print("0 is not a perfect number")
else:
    for el in range(1, num):
        if num % el == 0:
            print(el) 
            perfectNum = perfectNum + el 

    if perfectNum == num:
        print(num,"is a perfect number") 
    else:
        print(num,"is not a perfect number")