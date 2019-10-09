#Try at a numbers game 1 
import random
number = random.randint(1,20)
name = input("What is your name?> ")

print(f"Ok {name} I'm thinking of a number between 1 and 20.", '\n')
guess = int(input("What is your first guess?> "))

def game(guess):
    if guess == number:
        print("Correct!")
    elif guess > number:
        guess = int(input("Try a lower number> "))
        game(guess)
    else:
        guess = int(input("Try a higher number> "))
        game(guess)
game(guess)

#this is so if you run in cmd it stays open
input()