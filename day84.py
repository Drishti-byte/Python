#program to create a login screen (Advanced Version) 
from tkinter import * 
def welcomeMsg():
    name = usertxt.get() 
    pwd = pwdtxt.get() 
    if name == "admin" and pwd == 123:
        msg.configure(text = "Welcome Admin!!!!")
    else:
        msg.configure(text = "Welcome " + name + " !!!!")
def goodbyeMsg():
    name = usertxt.get() 
    pwd = pwdtxt.get() 
    if name == "admin" and pwd == 123:
        msg.configure(text = "Goodbye Admin!!!!")
    else:
        msg.configure(text = "Goodbye " + name + " !!!!")
scr = Tk() 
scr.title("Login Form") 
scr.geometry("1000x500") 
username = Label(scr, text = "Username:") 
username.place(x = 400, y = 100)
usertxt = Entry(scr) 
usertxt.place(x = 500, y = 100)
pwd = Label(scr, text = "Password:")
pwd.place(x = 400, y = 200)
pwdtxt = Entry(scr, show = "*") 
pwdtxt.place(x = 500, y = 200) 
loginbtn = Button(scr, text = "Login", command = welcomeMsg) 
loginbtn.place(x = 440, y = 250) 
logoutbtn = Button(scr, text = "Logout", command = goodbyeMsg) 
logoutbtn.place(x = 500, y = 250)
msg = Label(scr, text = "Message:") 
msg.place(x = 430, y = 300)
footer = Label(scr, text = "Thanks for visiting") 
footer.place(x = 450, y = 400)
scr.mainloop()