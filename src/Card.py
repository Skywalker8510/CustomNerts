class Card:
    def __init__(self, identifier, suit):
        self.identifier = identifier #numerical identifier 1 through 15 for
        self.suit = suit


    def get_identifier(self):
        return self.identifier


    def get_suit(self):
        return self.suit
    