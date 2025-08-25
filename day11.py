#program to print multiplication table of a number 
num = int(input("Enter a number:")) 
p = 0
for i in range(1, 11):
    p = num * i
    print(num,"X",i,"=",p) 