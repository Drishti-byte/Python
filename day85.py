#program to implement a basic calculator using tkinter 
from tkinter import * 
def sumOfNumber():
    n1 = eval(num1txt.get())
    n2 = eval(num2txt.get())
    sum = n1 + n2 
    res.configure(text = "Sum: " + str(sum))
def subtract():
    n1 = eval(num1txt.get())
    n2 = eval(num2txt.get())
    diff = n1 - n2
    res.configure(text = "Difference: " + str(diff))
def multiply():
    n1 = eval(num1txt.get())
    n2 = eval(num2txt.get())
    mul = n1 * n2 
    res.configure(text = "Product: " + str(mul))
def divide():
    n1 = eval(num1txt.get())
    n2 = eval(num2txt.get())
    if n2 == 0:
        res.configure(text = "Division by zero is not possible.")
    else:
        quo = n1 / n2  
        res.configure(text = "Quotient: " + str(quo))
scr = Tk()
scr.geometry("1000x500")
scr.title("Calculator")
heading = Label(scr, text = "My Calculator", font = 16)
heading.place(x = 500, y = 50)
num1 = Label(scr, text = "Number 1:", font = 14)
num1.place(x = 400, y = 100)
num1txt = Entry(scr)
num1txt.place(x = 500, y = 100)
num2 = Label(scr, text = "Number 2:", font = 14)
num2.place(x = 400, y = 150)
num2txt = Entry(scr)
num2txt.place(x = 500, y = 150)
add = Button(scr, text = "+", font = 16, command = sumOfNumber)
add.place(x = 400, y = 200)
sub = Button(scr, text = "-", font = 16, command = subtract)
sub.place(x = 430, y = 200)
mul = Button(scr, text = "X", font = 16, command = multiply)
mul.place(x = 460, y = 200)
div = Button(scr, text = "/", font = 16, command = divide)
div.place(x = 500, y = 200)
res = Label(scr, text = "Result", font = 14)
res.place(x = 500, y = 300)
footer = Label(scr, text = "Thanks for Visiting", font = 13)
footer.place(x = 450, y = 400)
scr.mainloop()