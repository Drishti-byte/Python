#program to read data from the file line by line 
f = open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close() 