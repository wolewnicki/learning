#Try at a numbers game 1
#DISCLAIMER: you have to run this with 2 arguments in something like powershell
from sys import argv 
script, x, y = argv
x = int(x)
y = int(y)
play = True
import random
number = random.randint(x,y)
name = input("What is your name?> ")

print(f"Ok {name} I'm thinking of a number between {x} and {y}.", '\n')

while ValueError:
    try:
        guess = int(input("What is your guess> "))
    except ValueError:
        print('\n', "Please enter a number", '\n')
        continue
    else: 
        break

#this is the main loop       
while play:
    try:
        if guess > number: 
            guess = int(input("Try a lower number> "))
            continue
        elif guess == number:
            print("Correct")
            again = str(input("Would you like you play again?> "))
            if again == "yes":
                number = random.randint(x,y)
                print(f"{name} thinking of a new number between {x} and {y}")
                guess = int(input("Enter a guess> "))
            else:
                print('\n', "Thanks for playing!", '\n')
                exit()
        else:
            guess = int(input("Try a higher number> "))
            continue
    except ValueError:
            print('\n', "Invalid please try again", '\n')
            continue

            
#this is so if you run in cmd it stays open
input()
