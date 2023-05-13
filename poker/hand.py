class Hand():
    def __init__(self,cards):
        card_copy = cards[:]
        card_copy.sort()
        self.cards = card_copy


    @property
    def _rank_validation_from_best_to_worst(self):
        return(
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", self._four_of_a_kind),
            ("Full House", self._full_house),
            ("Flush", self._flush),
            ("Straight", self._straight),
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", self._two_pair),
            ("Pair", self._pair),
            ("High Card", self._high_card)
        )

    def best_rank(self):
        for rank in self._rank_validation_from_best_to_worst:
            name, validator_func = rank
            if validator_func():
                return name

        # card_rank_count ={}
        # for card in self.cards:
        #     card_rank_count.setdefault(card.rank, 0)
        #     card_rank_count[card.rank] += 1

        # rank_with_three_of_a_kind = {
        #     rank:rank_count
        #     for rank, rank_count in self._card_rank_counts.items()
        #     if rank_count == 3
        # }
        # rank_with_three_of_a_kind = self._rank_with_count(3)
        # if len(rank_with_three_of_a_kind) == 1:
        #     return "Three of a Kind"
    
        # rank_with_pairs = {
        #     rank:rank_count
        #     for rank, rank_count in self._card_rank_counts.items()
        #     if rank_count == 2
        # }

        # rank_with_pairs = self._rank_with_count(2)
        # if len(rank_with_pairs) == 2:
        #     return "Two Pair"
        
        # if len(rank_with_pairs) == 1:
        #     return "Pair"
        
        # for rank_count in card_rank_count.values():
        #     if rank_count == 2:
        #         return "Pair"
        
        # return "High Card"
        
    
    
    def _rank_with_count(self, count):
        return {
            rank:rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }
    
    def _royal_flush(self):
        is_straight_flush = self._straight_flush()
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal

    def _straight_flush(self):
        return self._straight() and self._flush()
    
    def _four_of_a_kind(self):
        rank_with_three_of_a_kind = self._rank_with_count(4)
        return len(rank_with_three_of_a_kind) == 1
    
    def _full_house(self):
        return self._three_of_a_kind() and self._pair()
    
    def _flush(self):
        suits_that_occur_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
        return len(suits_that_occur_5_or_more_times) == 1
    
    def _straight(self):
            if len(self.cards) < 5:
                return False
            
            rank_indexes = [card.rank_index for card in self.cards]
            starting_rank_index = rank_indexes[0]
            ending_rank_index = rank_indexes[-1]
            straight_consecutive_card_index = list(range(starting_rank_index, ending_rank_index + 1))
            return rank_indexes == straight_consecutive_card_index
    
    def _three_of_a_kind(self):
         rank_with_three_of_a_kind = self._rank_with_count(3)
         return len(rank_with_three_of_a_kind) == 1
    
    def _two_pair(self):
        rank_with_pairs = self._rank_with_count(2)
        return len(rank_with_pairs) == 2
    
    def _pair(self):
         rank_with_pairs = self._rank_with_count(2)
         return len(rank_with_pairs) == 1
    
    def _high_card(self):
        return True
    
    @property
    def _card_rank_counts(self):
        card_rank_count ={}
        for card in self.cards:
            card_rank_count.setdefault(card.rank, 0)
            card_rank_count[card.rank] += 1
        return card_rank_count
    
    @property
    def _card_suit_counts(self):
        card_suit_count ={}
        for card in self.cards:
            card_suit_count.setdefault(card.suit, 0)
            card_suit_count[card.suit] += 1
        return card_suit_count