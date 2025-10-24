#program to create a login screen 
login = {"Drishti_123" : "123", "user" : "user@123", "hello" : "hello@123", "Drishti" : "d_123"} 
for k in range(3):
    userid = input("Enter username:") 
    password = input("Enter password:") 
    if userid in login.keys() and password in login.values():
        print("Correct credentials") 
        print("Access Granted!!!") 
        break 
    else:
        print("Invalid username or password") 
else:
    print("Access Denied!!")  