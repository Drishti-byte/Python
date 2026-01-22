#program to create a function to find the factorial 
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial is",fact)
num = int(input("Enter a number:"))
factorial(num)