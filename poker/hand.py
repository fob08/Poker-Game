class Hand():
    def __init__(self,cards):
        self.cards = cards

    def best_rank(self):
        # card_rank_count ={}
        # for card in self.cards:
        #     card_rank_count.setdefault(card.rank, 0)
        #     card_rank_count[card.rank] += 1

        # rank_with_three_of_a_kind = {
        #     rank:rank_count
        #     for rank, rank_count in self._card_rank_counts.items()
        #     if rank_count == 3
        # }
        rank_with_three_of_a_kind = self._rank_with_count(3)
        if len(rank_with_three_of_a_kind) == 1:
            return "Three of a Kind"
         
        # rank_with_pairs = {
        #     rank:rank_count
        #     for rank, rank_count in self._card_rank_counts.items()
        #     if rank_count == 2
        # }
        
        rank_with_pairs = self._rank_with_count(2)
        if len(rank_with_pairs) == 2:
            return "Two Pair"
        
        if len(rank_with_pairs) == 1:
            return "Pair"
        
        # for rank_count in card_rank_count.values():
        #     if rank_count == 2:
        #         return "Pair"
        
        return "High Card"
    
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