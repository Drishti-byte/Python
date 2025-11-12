#program to check whether a number is automorphic or not (last digit of square = number)
def automorphic(num):
    n = len(str(num))
    square = num ** 2 
    d = square % 10 ** n 
    return d 

num = int(input("Enter a number:")) 
res = automorphic(num)
if num == res:
    print(num, "is automorphic") 
else:
    print(num, "is not automorphic") 