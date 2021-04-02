from argparse import ArgumentParser

from cardgame.classes.cardgame import NeedMorePlayers, MaxPlayersHit
from cardgame.classes.cardgame_draw3 import Draw3Game

parser = ArgumentParser(description="Plays the Draw3 card game")
parser.add_argument(
    '--player_names',
    help='comma-delimited list of player names'
)
args = parser.parse_args()

if args.player_names:
    players_raw = args.player_names.split(',')
    player_names = []
    for player_name in players_raw:
        player_names.append(player_name.strip())
else:
    player_names = ['Buck', 'Cherry']

game = Draw3Game()

try:
    game.setup_game(player_names=player_names)
except MaxPlayersHit:
    print(f"Too many players.  Max players is {game.max_players}")
    exit(1)

try:
    game.start_game()
except NeedMorePlayers:
    print(f"Not enough players.  Need a minimum of {game.min_players}")
    exit(1)

while not game.is_game_over():
    game.next_turn()

player_rankings = game.player_rankings()
# print(player_rankings)
player = player_rankings[0]
print(f"{player.name} won with {player.score} points")
