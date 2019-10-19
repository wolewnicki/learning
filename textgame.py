from sys import exit
import random
money = 100
day = 0
def start():
    start = True
    print("Welcome to DopeWars!")
    print("You are in a city where drugs are legal!")
    print("Your goal is to make as much money as possible.")
    print(f"You currently have ${money}. Good luck!")
    print("Would you like to buy or hit the street.")
    
    while start:
        choice = input("> ")
        if choice == "buy":
            start = False
            store()
        elif choice == "street":
            start = False
            street()
        else: 
            print("Please enter 'buy' or 'street'")

def store():
    buy = True
    global money
    print("Welcome!")
    print("You can buy Weed for $10 or Coke for $100")

    while buy:
        choice = input("> ")
        if choice == "weed":
            print("You get 1 gram of weed")
            money = money - 10
            print(f"You now have ${money}")
            buy = False
            new_day()
        elif choice == "coke":
            print("You get 1 gram of coke")
            money = money - 100
            print(f"You now have ${money}")
            buy = False
            new_day()
        else:
            print("Are you gonna buy something or what?")

def new_day():
    global money
    print('\n', "A new day begins", '\n')
    number = random.randint(1,100)
    if number > 10 < 30:
        print("You have been mugged and lose 10$")
        money = money - 10
        street()
    elif number > 90:
        print("You were arrested for possesion")
        dead()
    elif number > 30 < 50:
        print("You find $10 when you wake up")
        street()
    elif number < 10:
        print("You were stabbed in the night and die")
        dead()
    else:
        print("It's a lovely day to buy some drugs")
        street()

def street():
    street = True
    print("You hit the streets looking for someone to sell to.")
    print("You could also go and buy more product if you want.")
    print("Or you could just wander the street.")

    while street: 
        choice = input("> ")
        if choice == "buy":
            street = False
            store()
        elif choice == "sell":
            street = False
            sell()
        elif choice == "wander":
            street = False
            wander()
        else: 
            print("Well pick something instead of just standing there!")

def sell():
    sell = True
    global money
    print("You find some lonely kid who might be interested.")
    print("You could sell it to him reasonably or jack the price")
    print("Sell 'high or 'low'?")

    while sell:
        choice = input("> ")
        if choice == "high":
            print("The kid realizes you're messing with him.")
            print("The kid had a gun on him and shoots you.")
            dead()
        elif choice == "low":
            print("The kid notices it's a good deal")
            money = money + 10
            print(f"You now have ${money}")
            sell = False
            street()
        else:
            print("The kid thinks you're messing with him and he leaves")
            street()


def wander():
    print("You aimlessly wander the streets until you run into a fight!")
    print("You enter the fight and get stabbed by some crackwhore and die")
    dead()

def dead():
    exit(0)




start()