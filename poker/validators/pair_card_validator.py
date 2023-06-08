from poker.validators import RankValidator


class PairValidator(RankValidator):
    def __init__(self, cards) -> None:
        self.cards = cards
        self.name = "Pair Card"

    def is_valid(self):
        rank_with_pairs = self._rank_with_count(2)
        return len(rank_with_pairs) == 1
    
    def valid_cards(self):
        rank_with_pairs = self._rank_with_count(2)
        cards = [card for card in self.cards if card.rank in rank_with_pairs.keys()]
        return cards
    