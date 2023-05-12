import unittest
from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_the_deck_is_initialy_empty(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_add_card_to_its_deck(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards, [card]
        )