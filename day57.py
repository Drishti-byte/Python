#program to validate a name entered by the user 
def validateName(name):
    if len(name) > 30:
        return False 
    for ch in name:
        if not (ch.isalpha() or ch == " "):
            return False 
    else:
        return True 
    
name = input("Enter a name:") 
if validateName(name):
    print(name, "is a valid name") 
else:
    print(name, "is not a valid name")