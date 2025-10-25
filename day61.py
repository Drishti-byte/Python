#program to count the number of vowels in a text file 
f = open("story.txt", "w") 
f.write("Hello World! I am doing file handling in Python. It's fun.\n") 
f.write("It is created using Python program. Interesting right?") 
f.close() 
f1 = open("story.txt", "r") 
data = f1.read()  
print(data)
vowel = 0
for ch in data:
    if ch in "AEIOUaeiou": 
        vowel += 1 
print("The number of vowels:",vowel) 
f1.close() 