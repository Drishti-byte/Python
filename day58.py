#program to validate phone number entered by the user 
def validatePhone(phone):
    if len(phone) != 10:
        return False 
    elif phone[0] not in ("789"):
        return False 
    elif not phone.isdigit():
        return False 
    else:
        return True 
    
phone = input("Enter a contact to validate:")
if validatePhone(phone):
    print("Phone number is VALID") 
else:
    print("Phone number is INVALID")