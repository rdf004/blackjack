from player import Player
from game_driver import play_game

MAX_PLAYERS = 10

# Ask how many players are playing?
num_players = int(input(">>> How many players will be playing? "))

# Check that number of players is less than MAX_PLAYERS
while num_players > MAX_PLAYERS:
    num_players = int(input(">>> {} is too many players, please choose fewer players. How many players will be playing? ".format(str(num_players))))

players = {}

# Choose names and create profiles for players
for i in range(num_players):
    name = str(input(">>> What is Player {}'s name? ".format(str(i+1))))
    while name in players.keys():
        name = str(input(">>> The name you chose was already chosen by someone else. Choose another name for Player {}? ".format(str(i+1))))
    if name not in players.keys():
        players[name] = Player(name)

print("Players are ", players)
play_game(players)

