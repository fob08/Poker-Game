class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
             "Jack", "Queen", "King", "Ace")
    
    @classmethod
    def create_standard_52_cards(cls):
        cards = []
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                cards.append(cls(rank = rank,suit = suit))
        return cards



    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank)
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank, your rank is {self.rank}. Your rank can be any of {self.RANKS}")
        
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit, your suit is {self.suit}, your suit can be one of {self.SUITS}")

        

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self) -> str:
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, other: object) -> bool:
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank_index < other.rank_index
    
    