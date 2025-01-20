from player import Player

Player1 = Player("Player1")
Player2 = Player("Player2")


print(f"{Player1.player_name}'s Nerts Pile:")
i = 1
for card in Player1.nerts_pile:
    print(f"{i} {card.get_identifier()} of {card.get_suit()}")
    i = i + 1

print(f"\n{Player2.player_name}'s Nerts Pile:")
for card in Player2.nerts_pile:
    print(f"{card.get_identifier()} of {card.get_suit()}")

print("\n\n")

print(Player1.player_name)
for card in Player1.player_deck.deck:
    print(f"{card.get_identifier()} of {card.get_suit()}")

print("\n\n")

print(Player2.player_name)
for card in Player1.player_deck.deck:
    print(f"{card.get_identifier()} of {card.get_suit()}")

print("")
dealt_card = Player1.player_deck.deal()
print (f"{dealt_card.get_identifier()} of {dealt_card.get_suit()}")

print("")
dealt_card = Player2.player_deck.deal()
print (f"{dealt_card.get_identifier()} of {dealt_card.get_suit()}")