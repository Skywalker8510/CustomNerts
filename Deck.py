from Card import Card
import random


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = []
        for i in range(0,4):
            for j in range(0,13):
                self.deck.append(Card(j+1,suits[i]))
        random.shuffle(self.deck)

    def get_deck(self, i):
        return self.deck[i]

    def deal(self):
        return self.deck.pop()