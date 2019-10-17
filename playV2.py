#variation of game with a function instead
import random

name = input("What is your name?> ")

def guessNumber():
    global number, guess, play
    number = random.randint(1,20)
    play = True
    while ValueError:
        try:
            guess = int(input(f"OK {name} what is your guess> "))
        except ValueError:
            print('\n', "Invalid please enter a number", '\n')
            continue
        else:
            break
            
guessNumber()      
      
while play:
    try:
        if guess > number: 
            guess = int(input("Try a lower number> "))
            continue
        elif guess == number:
            print("Correct")
            again = str(input("Would you like to play again?> "))
            if again == "yes":
                guessNumber()
            else:
                print('\n,', "Thank you for playing", '\n')
                exit()
        else:
            guess = int(input("Try a higher number> "))
            continue
    except ValueError:
            print('\n', "Invalid please try again", '\n')
            continue
        
