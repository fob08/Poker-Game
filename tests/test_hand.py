import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):
    def test_receives_and_store_cards(self):
        cards = [
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "Ace", suit = "Clubs")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.cards, cards)

    def test_figures_out_high_card_best_rank(self):
        cards = [
            Card(rank = "7", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_out_pair_is_the_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), "Pair")

    def test_figures_out_two_pair_is_the_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Spades"),
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "King", suit = "Clubs")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )

    def test_figures_out_three_of_a_kind_is_the_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "King", suit = "Clubs")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )
