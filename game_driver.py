from deck_manager import create_deck, draw

import random

deck = []
card_value = {}


def initialize_hands(players):
    for p in players.keys():
        player = players[p]

        card1, card2 = draw(deck, 2)
        player.cards.append(card1)
        player.cards.append(card2)
        player.hidden_card = card1
        player.public_hand.append(card2)
        player.total = card_value[card1] + card_value[card2]


def assign_random_nums(players):
    for i in players.keys():
        rand = random.randint(1, 10)
        players[i].num_added = ""
        print(">>> {}, your random number is {}.".format(i, str(rand)))

# Stand
def stand(player, split):
    return True

# Hit
def hit(player, split):
    global deck

    card = draw(deck, 1)
    if split:
        if player.split == True:
            player.split_cards.append(card)
            player.split_public_hand.append(card)
            # update Total
            return True
        else:
            print("You haven't split your cards.")
            return False

    else:
        player.cards.append(card)
        player.public_hand.append(card)
        return True

# Double Down
def double_down(player, split):
    player.bet = player.bet * 2
    player.account = player.account - player.bet

    global deck
    card = draw(deck, 1)
    if split:
        if player.split == True:
            player.split_cards.append(card)
            player.split_public_hand.append(card)
            # update Total
            return True
        else:
            print(">>> You haven't split your cards.")
            return False
    else:
        player.cards.append(card)
        player.public_hand.append(card)
        # update Total
        return True

# Split
def split(player, value):
    if user_can_split(player, value):
        player.cards.remove(value)
        player.public_hand.remove(value)
        # I don't think it matters if the value is the hidden card

        split = True
        split_cards.append(value)
        split_hidden_card = value
        split_total += card_value[value]

        return True
    else:
        print(">>> You don't have enough cards of that value to split on that value.")
    
# Check if user can split
def user_can_split(player, value):
    cards_count = {}
    for i in player.cards:
        cards_count[i] = cards_count.get(i, 0) + 1
    
    if cards_count[value] > 1:
        return True
    else:
        return False


# Surrender
def surrender(player):
    if player.split == False and len(player.cards) == 2:
        player.bet -= int(float(player.bet)/2.0)
        player.cards = []
        player.hidden_card = ''
        player.public_hand = ['*']
        player.total = 0

        card1, card2 = draw(deck, 2)
        player.cards.append(card1)
        player.cards.append(card2)
        player.public_hand.append(card2)
        player.hidden_card = card1
    else:
        print(">>> Too late for you to surrender ;)")
        return False

def handle_turn(player):
    action = str(input("What would you like to do? "))
    if action == "stand":
        stand(player, False)
        print(player.cards)

    elif action == "hit":
        hit(player, False)
        print(player.cards)

    elif action == "split":
        split(player)
        print(player.cards)

    elif action == "surrender":
        surrender(player)
        print(player.cards)

    elif action == "double down":
        double_down(player, False)
        print(player.cards)

def play_game(players):
    global deck
    global card_value

    deck, card_value = create_deck()
    initialize_hands(players)

    for i in players.keys():
        while True:
            handle_turn(players[i])

