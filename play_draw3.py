"""
play_draw3

Plays Draw 3 card game

for instructions on how to play:
python play_draw3.py -h
"""


import sys
from argparse import ArgumentParser

from cardgame.classes.cardgame import NeedMorePlayers, MaxPlayersHit
from cardgame.classes.cardgame_draw3 import Draw3Game


def new_round(round_num):
    """
    method to override cardgame_draw3.Draw3Game().new_round()
    so we can print out the round number

    (only gets set when --verbose flag is used)
    """
    print(f"Round #{round_num}")


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
    player_check = []
    for player_name in players_raw:
        new_player = player_name.strip()
        if new_player.lower() in player_check:
            print(
                (
                    "Please make sure each player name is unique.  ",
                    "{new_player} appears more than once."
                )
            )
            sys.exit(1)

        player_names.append(new_player)
        player_check.append(new_player.lower())
else:
    player_names = ['Buck', 'Cherry']

game = Draw3Game()

try:
    game.setup_game(player_names=player_names)
except MaxPlayersHit:
    print(f"Too many players.  Max players is {game.max_players}")
    sys.exit(1)

try:
    if args.verbose:
        print("\nStarting game...\n")
        # verbose is set, so print round numbers
        game.new_round = new_round

    if args.random_off:
        game.random_turn_order = False
    elif args.verbose:
        print("Randomizing turn order")

    game.start_game()
except NeedMorePlayers:
    print(f"Not enough players.  Need a minimum of {game.min_players}")
    sys.exit(1)

if args.verbose:
    NAMES = ', '.join(
        [
            p.name for p in game.get_current_players()
        ]
    )

    print(f"Players are:  {NAMES}")

while game.next_turn() is not None:
    player = game.get_current_player()

    if args.verbose:
        card = player.hand[-1]
        print(f"{player.name} drew a {card.value} of {card.suit}")

player_rankings = game.player_rankings()

if player_rankings is None:
    print("Could not get player rankings.")
    sys.exit(2)

winners = []
for player in player_rankings:
    if len(winners):  # pylint:  disable-msg=C1801
        if player.score < winners[-1].score:
            break

    winners.append(player)

NUM_WINNERS = len(winners)

if NUM_WINNERS == 0:
    print("\nUnable to determine winners.")
    sys.exit(3)

if NUM_WINNERS == 1:
    player = winners[0]
    print(f"\n{player.name} won with {player.score} points")
else:
    if NUM_WINNERS > 2:
        TIE_TYPE = f"{NUM_WINNERS}-way "
    else:
        TIE_TYPE = ""

    player = winners.pop()
    NAMES = " and ".join(
        [
            ", ".join(
                [
                    p.name for p in winners
                ]
            ),
            player.name
        ]
    )

    print(f"\nIt's a {TIE_TYPE}tie between {NAMES} at {player.score} points!")
