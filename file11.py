#program to print the table of a number in a file 
num = int(input("Enter a number:")) 
f = open("table.txt","w") 
p = 1
for i in range(1, 11):
    p = num * i
    f.write(f"{num} X {i} = {p}")
    f.write("\n")
print("File created and data has been written.") 