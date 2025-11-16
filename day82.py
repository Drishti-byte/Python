#program to count the occurences of a and m letters in story.txt 
with open("story.txt", "r") as f:
    data = f.read()
    countA = 0
    countM = 0
    for ch in data:
        if ch in "aA":
            countA += 1 
        elif ch in "mM":
            countM += 1
print("The number of occurences of a/A are:", countA) 
print("The number of occurences of m/M are:",countM)