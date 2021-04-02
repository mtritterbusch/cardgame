from argparse import ArgumentParser

from cardgame.classes.cardgame import NeedMorePlayers, MaxPlayersHit
from cardgame.classes.cardgame_draw3 import Draw3Game

parser = ArgumentParser(description="Plays the Draw3 card game")
parser.add_argument(
    '--players',
    help='comma-delimited list of player names'
)
parser.add_argument(
    '--verbose',
    help='Verbose feedback of game progress',
    action='store_true'
)
parser.add_argument(
    '--random_off',
    help='Do not randomize turn order',
    action='store_true'
)
args = parser.parse_args()

if args.players:
    players_raw = args.players.split(',')
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
    if args.verbose:
        print("\nStarting game...\n")

    if args.random_off:
        game.random_turn_order = False
    elif args.verbose:
        print("Randomizing turn order")

    game.start_game()
except NeedMorePlayers:
    print(f"Not enough players.  Need a minimum of {game.min_players}")
    exit(1)

if args.verbose:
    names = ', '.join(
        [
            p.name for p in game.get_current_players()
        ]
    )

    print(f"Players are:  {names}")

while not game.is_game_over():
    player = game.next_turn()
    if args.verbose:
        card = player.hand[-1]
        print(f"{player.name} drew a {card.value} of {card.suit}")

player_rankings = game.player_rankings()

winners = []
for player in player_rankings:
    if len(winners):
        if player.score < winners[-1].score:
            break

    winners.append(player)

num_winners = len(winners)

if num_winners == 1:
    player = winners[0]
    print(f"\n{player.name} won with {player.score} points")
else:
    if num_winners > 2:
        tie_type = f"{num_winners}-way "
    else:
        tie_type = ""

    player = winners.pop()
    names = " and ".join(
        [
            ", ".join(
                [
                    p.name for p in winners
                ]
            ),
            player.name
        ]
    )

    print(f"\nIt's a {tie_type}tie between {names} at {player.score} points!")
