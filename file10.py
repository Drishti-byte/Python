#proram to count the number of vowels in the file 
f = open("mystory.txt", "r")
data = f.read()
vow = 0 
for ch in data:
    if ch in "AEIOUaeiou":
        vow += 1 
print(data) 
print()
print("Number of vowels are:",vow) 
f.close()