import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
     def setUp(self):
         self.six_of_clubs = Card(rank = "6", suit = "Clubs"),
         self.six_of_diamonds = Card(rank = "6", suit = "Diamonds"),
         self.six_of_spades = Card(rank = "6", suit = "Spades"),
         self.nine_of_clubs = Card(rank = "9", suit = "Clubs"),
         self.nine_of_spades = Card(rank = "9", suit = "Hearts")
        
         self.cards = [
             self.six_of_clubs,
             self.six_of_diamonds,
             self.six_of_spades,
             Card(rank = "5", suit = "Clubs"),
             self.nine_of_clubs,
             self.nine_of_spades,
             Card(rank = "Queen", suit = "Diamonds")
         ]
     def test_validates_that_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):
          validator = FullHouseValidator(cards = self.cards)
          self.assertEqual(validator.is_valid(), True)

     def test_return_collection_of_two_cards_of_the_same_rank_and_three_cards_of_the_same_rank(self):
         validator = FullHouseValidator(cards = self.cards)
        
         self.assertEqual(validator.valid_cards(), 
                          [
                               self.six_of_clubs,
                               self.six_of_diamonds,
                               self.six_of_spades,
                               self.nine_of_clubs,
                               self.nine_of_spades,
                          ])