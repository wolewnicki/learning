#Try at a numbers game 1 
import random
number = random.randint(1,20)
name = input("What is your name?> ")

print(f"Ok {name} I'm thinking of a number between 1 and 20.", '\n')

while True:
    try:
        guess = int(input("What is your guess> "))
    except ValueError:
        print('\n', "Please enter a number", '\n')
        continue
    else: 
        break

#this is the main loop       
while True:
    try:
        if guess == number:
            print("Correct!")
            break
        elif guess > number: 
            guess = int(input("Try a lower number> "))
            continue
        else:
            guess = int(input("Try a higher number> "))
            continue
    except ValueError:
            print('\n', "Invalid please try again", '\n')
            continue
#this is so if you run in cmd it stays open
input()
