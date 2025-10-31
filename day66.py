#program to print a name using letter images 
import pygame 
name = input("Enter your name:") 
pygame.init() 
clr = (255, 255, 255)
w = len(name) * 120 + 100 
win = pygame.display.set_mode((w, 400))
pygame.display.set_caption("Display name using images") 
letters = "abcdefghijklmnopqrstuvwxyz" 
img = {} 
for ch in letters:
    try:
        img[ch] = pygame.image.load(f"{ch}.png")
    except:
        img[ch] = pygame.image.load(f"{ch}.jpg")
width , height = 100 , 100 
for ch in img:
    img[ch] = pygame.transform.scale(img[ch], (width, height)) 
image = [] 
for ch in name.lower():
    image.append(img[ch]) 
while True:
    win.fill(clr) 
    x = 50
    for i in image:
        win.blit(i, (x, 150))
        x += width + 20 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            quit() 
    pygame.display.update()