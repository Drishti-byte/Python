#program to check whether the string is palindrome or not 
txt = input("Enter a string:")
isPalindrome = True 
for i in range(0, (len(txt) // 2) + 1): 
    if txt[i] != txt[-(i + 1)]:         #for i in range(len(txt) - 1, -1, -1): #rev[::-1]
        isPalindrome = False 
if isPalindrome == True:
    print("String is palindrome") 
else: 
    print("String is not palindrome") 