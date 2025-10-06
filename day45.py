#program to count the number of vowels in a string 
s = input("Enter a string:")
count = 0
for ch in s:
    if ch in "AEIOUaeiou":
        count = count + 1
print("Number of vowels in the string are:",count) 

#program to count number of alphabets, digits and spaces in a string 
# s = input("Enter a string:")
# alphanum = 0 
# digits = 0 
# spaces = 0 
# for ch in s:
#     if ch.isalpha():
#         alphanum += 1 
#     elif ch.isdigit():
#         digits += 1 
#     elif ch.isspace():
#         spaces += 1 
# print("String entered by the user is", s)
# print("Number of alphabets in the string are:",alphanum) 
# print("Number of digits in the string are:",digits) 
# print("Number of spaces in the string are:",spaces) 