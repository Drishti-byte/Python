#program to create a login form using GUI 
from tkinter import * 
def check():
    username = nametxt.get()
    passw = pwdtxt.get() 
    print("Username Entered:",username) 
    print("Password Entered:",passw) 

scr = Tk() 
scr.geometry("900x450")
scr.title("Login / Signup Form") 
username = Label(scr, text = "Username:") 
username.grid(row = 0, column = 0) 
nametxt = Entry(scr) 
nametxt.grid(row = 0, column = 4) 
pwd = Label(scr, text = "Password:")
pwd.grid(row = 1, column = 0) 
pwdtxt = Entry(scr, show = "*")
pwdtxt.grid(row = 1, column = 4) 
loginbtn = Button(scr, text = "Login", command = check)
loginbtn.grid(row = 5, column = 0)
scr.mainloop()