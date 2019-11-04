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
            print(card.show())
    
    def build(self):
        self.contents = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for rank in range(1,14):
                self.contents.append(Card(rank, suit))
                
    def shuffle(self):
        for i in range(0, 53-1):
            j = random.randint(1, i + 1)
            self.contents[j], self.contents[i] = self.contents[i], self.contents[j]

#card = Card('6', 'Diamonds')
#card.show()
deck = Deck()
deck.shuffle()
deck.show()
