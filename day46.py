#program to reverse a string word by word 
str = input("Enter a string:") 
print(str)
strsplit = str.split() 
strsplit = strsplit[::-1] 
strjoin = " ".join(strsplit) 
print(strjoin) 