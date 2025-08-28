#program to find the factors of a number 
num = int(input("Enter a number:")) 
print("The factors of",num,"are:")

for el in range(2,num+1):
    if num % el == 0:
        print(el) 