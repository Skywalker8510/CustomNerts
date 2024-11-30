class NertsPile:
    @staticmethod
    def create_pile(player):
        player.nerts_pile = []
        for i in range (0,13):
            player.nerts_pile.append(player.player_deck.deal())