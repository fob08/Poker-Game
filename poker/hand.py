from poker.validators import (RoyalFlushValidator,
                              StraightFlushValidator,
                              FourOfAKindValidator,
                              FullHouseValidator,
                              FlushValidator,
                              StraightValidator,
                              ThreeOfAKindValidator,
                              TwoPairValidator,
                              PairValidator,
                              HighCardValidator,
                              NoCardsValidator
                              )

class Hand():
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator
    )
    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self,cards):
        card_copy = self.cards[:]
        card_copy.extend(cards)
        card_copy.sort()
        self.cards = card_copy

    def best_rank(self):
        for index, validator_class in enumerate(self.VALIDATORS):
            validator = validator_class(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())
            

    
    