#program to guess the number 
import random 
target = random.randint(1, 100)

while(True):
    userChoice = input("Guess the number or Quit(Q): ")
    if(userChoice == "Q"):
        break 
    userChoice = int(userChoice)
    if(userChoice == target):
        print("SUCCESS: CORRECT GUESS!!")
        break 
    elif(userChoice < target):
        print("Your number is too small. Take a bigger guess..") 
    else:
        print("Your number is too big. Take a smaller guess..")
print("--------GAME OVER-------")