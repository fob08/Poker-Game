import unittest
from unittest.mock import patch

from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_has_length_that_is_equal_to_count_of_cards(self):
        deck = Deck()
        self.assertEqual(
            len(deck), 0
        )
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

    @patch('random.shuffle')
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds")
        ]
        
        deck.add_cards(cards)
        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_remove_specified_number_of_cards_from_deck(self):
        ace = Card(rank = "Ace", suit = "Spades")
        seven = Card(rank = "7", suit = "Diamonds")
        cards = [ace,seven]

        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck.cards, [seven]
        )