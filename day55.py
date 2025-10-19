#program to check if the email is valid or not 
def isValidEmail(email):
    if email.endswith(".com"):
        if email[0] != "@" and email.count("@") == 1:
            for ch in email:
                if ch.isalpha() or ch.isdigit() or ch == "." or ch == "_" or ch == "@":
                    continue 
                else:
                    return False 
            else:
                return True 
        else:
            return False 
    else:
        return False  

email = input("Enter an email id:") 
if isValidEmail(email):
    print("Valid email id")
else:
    print("Not a valid email id") 