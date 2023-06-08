import random

class Deck():
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)
    
    def add_cards(self,cards):
        self.cards.extend(cards)

    def remove_cards(self, number_of_cards_to_remove):
        cards_to_remove = self.cards[:number_of_cards_to_remove]
        del self.cards[:number_of_cards_to_remove]
        return cards_to_remove
    
    def shuffle(self):
        random.shuffle(self.cards)