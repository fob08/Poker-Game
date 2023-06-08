class TwoPairValidator():
    def __init__(self,cards):
        self.cards = cards
        self.name = "Two Pair"

    def is_valid(self):
        rank_with_pairs = self._rank_with_count(2)
        return len(rank_with_pairs) == 2
    
    def valid_cards(self):
        rank_with_pairs = self._rank_with_count(2)
        cards = [card for card in self.cards if card.rank in rank_with_pairs.keys()]
        return cards
    
    def _rank_with_count(self, count):
        return {
            rank:rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }
    
    

    @property
    def _card_rank_counts(self):
        card_rank_count ={}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        return card_rank_count