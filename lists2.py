#program to check if a list contains a palindrome of elements or not 
list1 = [1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("Lists are palindrome")
else:
    print("Lists are not palindrome")