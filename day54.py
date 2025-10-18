#program to toggle case a string 
str = input("Enter a string:") 
# res = str.swapcase() 
res = ""
for ch in str:
    if ch.isupper():
        res += ch.lower() 
    elif ch.islower():
        res += ch.upper() 
    else:
        res += ch 
print("Original string:", str)  
print("Toggled string:", res) 

#program to convert string in toggle case (part 2) 
# str = input("Enter a string:") 
# res = ""
# for i in range(len(str)):
#     if i % 2 == 0:
#         res += str[i].upper() 
#     elif i % 2 != 0:
#         res += str[i].lower() 
#     else:
#         res += str[i] 
# print("Original string:", str) 
# print("Toggled string:", res) 