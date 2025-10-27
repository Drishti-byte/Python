#program to create a login screen using CSV file 
import csv 
username = input("Enter username:")
passw = input("Enter password:") 
f = open("login.csv", "r") 
cr = csv.reader(f) 
for row in cr:
    if row[0] == username and row[1] == passw:
        print("Welcome", username)
        print("Login successfull!!") 
        break 
else:
    print("Invalid username or password")
f.close()