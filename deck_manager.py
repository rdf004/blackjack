import random

# We will simulate a Continuous Shuffling Machine

def create_deck():
    card_value = {}

    NUM_SUITS = 4
    NUM_DECKS = 2
    variety = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']

    for i in range(len(variety)):
        if i < 9:
            card_value[variety[i]] = int(variety[i])
        elif i == len(variety) - 1:
            card_value[variety[i]] = 11
        else:
            card_value[variety[i]] = 10

    deck = []
    for i in range(len(variety)):
        for j in range(NUM_SUITS * NUM_DECKS):
            deck.append(variety[i])

    return deck, card_value

def draw(deck, num):
    index = random.randint(1, len(deck))
    card1 = deck[index]
    deck.pop(index)

    if num == 2:
        index2 = random.randint(1, len(deck))
        card2 = deck[index2]
        deck.pop(index2)

        return card1, card2
    
    return card1


