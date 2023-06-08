import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_validates_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank = "3", suit = "Spades"),
            Card(rank = "4", suit = "Spades"),
            Card(rank = "5", suit = "Spades"),
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Spades"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
        ]
        validator = StraightFlushValidator(cards = cards)


        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_validates_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank = "3", suit = "Spades"),
            Card(rank = "4", suit = "Spades"),
            Card(rank = "5", suit = "Spades"),
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Clubs"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        validator = StraightFlushValidator(cards = cards)


        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_determines_that_there_are_five_consecutive_cards_with_the_same_suit(self):
        three = Card(rank = "3", suit = "Spades"),
        four = Card(rank = "4", suit = "Spades"),
        five = Card(rank = "5", suit = "Spades"),
        six = Card(rank = "6", suit = "Spades"),
        seven = Card(rank = "7", suit = "Spades")
        
        cards = [
            three,
            four,
            five,
            six,
            seven,
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
            ]
        validator = StraightFlushValidator(cards = cards)


        self.assertEqual(
            validator.valid_cards(),
            [
                three,
                four,
                five,
                six,
                seven
            ]
        )