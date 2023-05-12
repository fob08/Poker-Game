import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank="3", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_has_rank_and_suit_string_representation(self):
        card = Card("9", "Spades")
        self.assertEqual(str(card), "9 of Spades")

    def test_has_technical_representation(self):
        card = Card(rank="3", suit = "Clubs")
        self.assertEqual(repr(card), "Card('3', 'Clubs')")

    def test_card_has_four_suit(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )
    
    def test_card_has_thirteen_rank(self):
        self.assertEqual(
            Card.RANKS,
            ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
             "Ace", "Queen", "Jack", "King")
        )

    def test_card_only_allow_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank ="Two", suit = "Hearts")

    def test_card_only_allow_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank ="2", suit = "Heart")