import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_card_have_a_high_card(self):
        cards = [
            Card(rank = "7", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        validator = HighCardValidator(cards = cards)

        self.assertEqual(validator.is_valid, True)

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")
        cards = [
            Card(rank = "7", suit = "Spades"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Queen", suit = "Spades"),
            ace_of_diamonds
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )