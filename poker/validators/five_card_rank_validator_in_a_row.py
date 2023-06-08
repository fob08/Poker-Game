class FiveCardRanksInARowValidator():
    @property
    def _collection_of_five_straight_cards_in_a_row(self):
        index = 0
        final_index = len(self.cards) - 1
        collection_of_five_straight_cards_in_a_row = []

        while index + 4 <= final_index:
             next_five_cards = self.cards[index: index + 5]
             next_five_raank_indices = [card.rank_index for card in next_five_cards]

             if self._every_element_increasing_by_1(next_five_raank_indices):
                  collection_of_five_straight_cards_in_a_row.append(next_five_cards)
             index += 1

        return collection_of_five_straight_cards_in_a_row 
        
    
    def _every_element_increasing_by_1(self, rank_indexes):
        starting_rank_index = rank_indexes[0]
        ending_rank_index = rank_indexes[-1]
        straight_consecutive_card_index = list(range(starting_rank_index, ending_rank_index + 1))
        return rank_indexes == straight_consecutive_card_index