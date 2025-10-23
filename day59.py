#program to check strength of a password 
def validatePassw(password):
    n = len(password)
    if not (n >= 8 and n <= 16):
        print("Length of the password should be between 8 - 16 characters")  
    else:
        u = 0
        l = 0
        a = 0
        d = 0 
        ss = 0 
        for ch in password:
            if ch.isupper():
                u += 1
            elif ch.islower():
                l += 1 
            elif ch.isdigit():
                d += 1 
            elif ch in "._@":
                ss += 1 
            else:
                a += 1
                break 
        if a != 0:
            print("Invalid password")
        else: 
            if u > 0 and l > 0 and d > 0 and ss > 0:
                print("Password strength is strong")
            else:
                print("Weak password")
password = input("Enter a password to validate:") 
validatePassw(password)