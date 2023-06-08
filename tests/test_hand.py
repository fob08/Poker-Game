import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])
    
    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank = "7", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
    def test_receives_and_store_cards(self):
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        seven_of_hearts = Card(rank = "7", suit = "Hearts")
        cards = [
            ace_of_clubs,
            seven_of_hearts
            
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.cards, 
                         [
                             seven_of_hearts,
                             ace_of_clubs
                         ])
    



    def test_figures_out_three_of_a_kind_is_the_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "King", suit = "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )
     
    def test_figures_out_straight_is_the_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "8", suit = "Spades"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card("2", "Hearts"),
            Card("3", "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_best_rank_when_flush(self):
        cards = [Card(rank = rank, suit = "Hearts") for rank in ["2","4","5","8", "King"]
                 ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Spades"),
            Card(rank = "6", suit = "Diamonds"),
            Card(rank = "6", suit = "Spades"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "9", suit = "Hearts")
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Spades"),
            Card(rank = "6", suit = "Diamonds"),
            Card(rank = "6", suit = "Spades"),
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "9", suit = "Clubs"),
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Spades"),
            Card(rank = "4", suit = "Spades"),
            Card(rank = "5", suit = "Spades"),
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Spades"),
        ]
        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "10", suit = "Spades"),
            Card(rank = "Jack", suit = "Spades"),
            Card(rank = "Queen", suit = "Spades"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Spades"),
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )

    
