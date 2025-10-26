#program to read a text file and display each word separated by # 
f = open("story.txt", "r") 
data = f.read().split()
for word in data:
    print(word, end = " # ") 
f.close() 