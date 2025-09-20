#program to make a dice game 

import random 
import pygame 
import time 

p = ["","","","","",""] 
p[0] = pygame.image.load("d1.jpg")
p[1] = pygame.image.load("d2.jpg")
p[2] = pygame.image.load("d3.jpg")
p[3] = pygame.image.load("d4.jpg")
p[4] = pygame.image.load("d5.jpg")
p[5] = pygame.image.load("d6.jpg")

name1 = input("Please enter the name of player 1:")
name2 = input("Please enter the name of player 2:")
val1 = random.randint(1,6)
val2 = random.randint(1,6) 

print("Player 1:",val1)
print("Player 2:",val2)

if val1 > val2:
    res = name1 + " WINS"
elif val1 < val2:
    res = name2 + " WINS"
else:
    res = "It's a DRAW" 
    
pygame.init() 
white = (255, 255, 255) 
pink = (255, 0, 127)
yellow = (255, 255, 0) 
font = pygame.font.Font('freesansbold.ttf',32)
text1 = font.render(name1, True, pink, yellow)
text2 = font.render(name2, True, pink, yellow) 
res = font.render(res, True, pink, yellow)

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = res.get_rect() 
textRect1.center = (150, 100)
textRect2.center = (350, 100)
textRect3.center = (250, 500) 
win = pygame.display.set_mode((600, 600)) 

while True:
    win.fill("black") 
    win.blit(text1, textRect1)
    win.blit(text2, textRect2)
    win.blit(res, textRect3) 
    win.blit(p[val1 - 1], (100, 200)) 
    win.blit(p[val2 - 1], (300, 200))
    time.sleep(5) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            quit() 
    pygame.display.update() 