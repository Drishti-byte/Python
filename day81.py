#program to create a bouncing ball using turtle 
import turtle 
import time 
def moveLeft():
    xc = ball.xcor() 
    ball.setx(xc - 10) 
def moveRight():
    xc = ball.xcor() 
    ball.setx(xc + 10) 
def moveUp():
    yc = ball.ycor() 
    ball.sety(yc + 10) 
def moveDown():
    yc = ball.ycor() 
    ball.sety(yc - 10)     
scr = turtle.Screen() 
scr.title("Bouncing Ball") 
scr.bgcolor("Pink") 
scr.setup(width = 600, height = 600) 
ball = turtle.Turtle() 
ball.shape("circle") 
ball.speed(0)
ball.color("blue")
ball.shapesize(stretch_len = 6, stretch_wid = 6) 
ball.penup() 
d = 0 
u = 0
while True:
    if d == 0 and u == 0:
        moveLeft() 
        moveDown()
    if d == 1 and u == 1:
        moveRight() 
        moveUp()
    if ball.xcor() >= 300:
        d = 0
    if ball.xcor() <= -300:
        d = 1
    if ball.ycor() >= 300:
        u = 0
    if ball.ycor() <= -300:
        u = 1 
    time.sleep(0.1) 
    scr.update() 