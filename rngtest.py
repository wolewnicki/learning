from sys import exit
import random
correct = 3
index = 0 

def start():
    global index, correct
    number = random.randint(1,100)
    while index < correct:
        if number == 69:
            print(f"Number was {number}. Nice. You win automatically")
            win("You got the sex number")
        elif number < 20 :
            game1()
        elif 20 < number < 40:
            game2()
        elif 40 < number < 60:
            game3()
        elif 60 < number < 80:
            game4()
        elif 80 < number <= 100:
            game5()
        else:
            win("you won because of a bug")
    while index == correct:
        win("you got enough correct")


def win(condition):
    print(f"Congratulations! You won because, {condition}! Good job!")
    input() #this is so if you run it in CMD it stays open
    exit(0)

def lose(lost):
    print(f"Somehow you lost this easy game because {lost}")
    input() #this is so if you run it in CMD it stays open
    exit(0)

def game1():
    global index
    print("What is 1 + 1")
    add = (input("> "))
    if add == "2":
        print("Correct!")
        index = index + 1
        start()
    else:
        print("How did you get this wrong?")
        lose("bad at adding")

def game2():
    global index
    print("What color is the sky")
    sky = input("> ")
    if sky == "blue":
        print("Correct!")
        index = index + 1
        start()
    else:
        print("How did you get this wrong.")
        lose("you're color blind")

def game3():
    global index
    print("Is the Earth round yes or no?")
    earth = input("> ")
    if earth == "yes":
        print("Correct")
        index = index + 1
        start()
    else:
        print("How did you get this wrong.")
        lose("you're a flat earther")

def game4():
    global index
    print("How many states are in the United states")
    states = input("> ")
    if states == "50":
        print("Correct!")
        index = index + 1
        start()
    else:
        print("How did you get this wrong")
        lose("you're a fake American")

def game5():
    global index
    print("I'm out of ideas just type 'z'")
    z = input("> ")
    if z == "z":
        print("Correct!")
        index = index + 1
        start()
    else:
        print("There is no way you can possibly get this wrong")
        lose("keyboard broken")
    

start()
