#program to create a game to guess a number 
import random 
num = random.randint(1, 100) 
guess_num = int(input("Guess the number(1-100): ")) 
while(guess_num != num):
    if guess_num > num:
        print("Guess a smaller number")
        guess_num = int(input("Guess the number(1-100): ")) 
    else:
        print("Guess a larger number")
        guess_num = int(input("Guess the number(1-100): ")) 
print("Congratulations !!! You guessed the number!!!")