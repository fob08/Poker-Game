import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank="3", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_knows_its_rank_index(self):
        card = Card(rank = "Queen", suit = "Clubs")
        self.assertEqual(card.rank_index, 10)

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
             'Jack', 'Queen', 'King', 'Ace')
        )

    def test_card_only_allow_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank ="Two", suit = "Hearts")

    def test_card_only_allow_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank ="2", suit = "Heart")

    def test_can_crate_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)
        self.assertEqual(cards[0], Card(rank = "2", suit = "Hearts"))
        self.assertEqual(cards[-1], Card(rank = "Ace", suit = "Diamonds"))

    def test_card_equality_check(self):
        self.assertEqual(
            Card("2", "Hearts"),
            Card("2", "Hearts")
        )

    def test_card_can_rank_itself_with_another_one(self):
        king_of_heart = Card(rank = "King", suit = "Hearts")
        queen_of_heart = Card(rank = "Queen", suit = "Hearts")
        comparison = queen_of_heart < king_of_heart
        self.assertEqual(
            comparison, True
            )

    def test_sort_cards(self):
        two_of_spades = Card(rank = "2", suit = "Spades")
        six_of_diamonds = Card(rank = "6", suit = "Diamonds")
        six_of_hearts = Card(rank = "6", suit = "Hearts")
        eight_of_spades = Card(rank = "8", suit = "Hearts")
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")

        unsorted_cards = [
            six_of_hearts,
            six_of_diamonds,
            eight_of_spades,
            two_of_spades,
            ace_of_clubs,
        ]
        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                six_of_diamonds,
                six_of_hearts,
                eight_of_spades,
                ace_of_clubs
            ]
        )
        
    