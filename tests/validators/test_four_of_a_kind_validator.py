import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.six_of_spades = Card(rank = "6", suit = "Spades")
        self.six_of_diamonds = Card(rank = "6", suit = "Diamonds")
        self.six_of_spades = Card(rank = "6", suit = "Spades")
        self.six_of_hearts = Card(rank = "6", suit = "Hearts")
        self.nine_of_clubs = Card(rank = "9", suit = "Clubs")
        self.cards = [
            Card(rank = "2", suit = "Clubs"),
            self.six_of_spades,
            self.six_of_diamonds,
            self.six_of_spades,
            self.six_of_hearts,
            Card(rank = "8", suit = "Diamonds"),
            self.nine_of_clubs
        ]
    def test_determine_that_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(cards=self.cards)


        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_return_the_four_cards_with_the_same_ranks(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.six_of_spades,
                self.six_of_diamonds,
                self.six_of_spades,
                self.six_of_hearts
            ]
        )