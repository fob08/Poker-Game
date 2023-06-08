import unittest

from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator

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


    def test_interacts_with_validator_to_get_wining_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator,)

        ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        cards = [ace_of_hearts, ace_of_spades]

        hand = HandWithOneValidator()
        hand.add_cards(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            (0, "Pair Card", [ace_of_hearts,ace_of_spades])
        )
