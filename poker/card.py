class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
             "Ace", "Queen", "Jack", "King")
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank, your rank is {self.rank}. Your rank can be any of {self.RANKS}")
        
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit, your suit is {self.suit}, your suit can be one of {self.SUITS}")

        

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self) -> str:
        return f"Card('{self.rank}', '{self.suit}')"
    