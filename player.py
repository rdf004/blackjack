class Player:
    def __init__(self, name):
        self.name = name
        self.account = 1000

        # Per game
        self.bet = 0
        self.still_playing = True


        # Player's hand
        self.cards = []
        self.hidden_card = ''
        self.public_hand = ['*']
        self.total = 0
        
        # If the player decides to split
        self.split = False
        self.split_cards = []
        self.split_hidden_card = ''
        self.split_public_hand = ['*']
        self.split_total = 0

        self.num_added = 0
        self.wins = 0
