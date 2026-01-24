#program to check whether the number is even or odd
def even_odd(num):
    for i in range(1,num + 1,1):
        if(num % 2 == 0):
            print(num,"is even")
            break
        else:
            print(num,"is odd")
            break
n = int(input("Enter a number: "))
even_odd(n)