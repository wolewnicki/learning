import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        if self.rank == 1:
            print(f"Ace of {self.suit}")
        elif self.rank == 11:
            print(f"Jack of {self.suit}")
        elif self.rank == 12:
            print(f"Queen of {self.suit}")
        elif self.rank == 13:
            print(f"King of {self.suit}")
        else:
            print(f"{self.rank} of {self.suit}")

class Deck:
    def __init__(self):
        self.build()

    def show(self):
        for card in self.contents:
            card.show()
    
    def build(self):
        self.contents = []
        for suit in suits:
            for rank in ranks:
                self.contents.append(Card(rank, suit))
                
    def shuffle(self):
        for i in range(0, 52):
            j = random.randint(0, i + 1)
            self.contents[j], self.contents[i] = self.contents[i], self.contents[j]
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']        
ranks = list(range(1,14))        
rankValues = {1 : 11,
              11 : 10,
              12 : 10,
              13 : 10}        

deck = Deck()
deck.shuffle()
deck.show()
