#program to read the data from the file and count the no of alphabets and digits. 
f = open("mystory.txt", "r") 
data = f.read() 
alphanum = 0
digits = 0
for ch in data:
    if ch.isalpha():
        alphanum += 1 
    elif ch.isdigit():
        digits += 1 
print(data)
print("Number of alphabets found in the file are:",alphanum) 
print("Number of digits found in the file are:",digits) 