import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
            five_of_clubs = Card(rank = "5", suit = "Clubs")
            self.king_of_clubs = Card(rank = "King", suit = "Clubs")
            self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
            self.king_of_spades = Card(rank = "King", suit = "Spades")
            Ace_of_hearts = Card(rank = "Ace", suit = "Hearts")

            self.cards =[
                 five_of_clubs,
                 self.king_of_clubs,
                 self.king_of_diamonds,
                 self.king_of_spades,
                 Ace_of_hearts
            ]
            

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        
        validator = ThreeOfAKindValidator(cards = self.cards)
        
        self.assertEqual(validator.is_valid(), True)

    def test_return_three_of_a_kind_cards_from_card_collection(self):
         validator = ThreeOfAKindValidator(cards = self.cards)
        
         self.assertEqual(validator.valid_cards(), 
                          [
                               self.king_of_clubs,
                               self.king_of_diamonds,
                               self.king_of_spades
                          ])