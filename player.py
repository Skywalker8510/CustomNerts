from Deck import Deck
from NertsPile import NertsPile


class Player:

    def __init__(self, name):
        self.player_name = name
        self.player_deck = Deck()
        self.points = 0
        NertsPile.create_pile(self)