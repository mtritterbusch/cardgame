import random

from cardgame.classes.cardgame import (
    CardGame,
    InvalidNumberOfPlayers,
    NeedMorePlayers
)
from cardgame.classes.deckmanager import DeckManager


class Draw3Game(CardGame):
    """
    Draw3Game:  2 players
        initial hand each player takes turns drawing a card up to 3
        points per card are (suit + 1) * value
        winner has highest number of points
    """
    def __init__(self):
        super().__init__()

        self._min_players = 2
        self._max_players = 8

        # this game only has 3 rounds
        self._num_rounds = 3
        self._turn_num = 0
        self._round_num = 0

    def setup_game(self, deck=None, player_names=['Fred', 'Sally']):
        if deck is None:
            # default to standard 52-card deck
            self._deck = DeckManager()
            self._deck.shuffle()
        else:
            self._deck = deck

        for player_name in player_names:
            self.add_player(player_name)

    def start_game(self, random_start=True):
        if len(self._players) < self.min_players:
            raise NeedMorePlayers
        elif len(self._players) > self.max_players:
            raise InvalidNumberOfPlayers

        if random_start:
            random.shuffle(self._turn_order)

    def is_game_over(self):
        return self._round_num >= self._num_rounds

    def get_current_player(self):
        return self._players[
            self._turn_order[
                self._turn_num
            ]
        ]

    def next_turn(self):
        # current player draws a card
        player = self.get_current_player()
        player.draw_card(self._deck)
        self._turn_num = (self._turn_num + 1) % len(self._players)
        if self._turn_num == 0:
            self._round_num += 1

    def calc_points(self, hand):
        points = 0
        for card in hand:
            points += card.suit_value * card.card_value

        return points

    def player_rankings(self):
        for player in self._players:
            player.score = self.calc_points(player.hand)

        players = self._players.copy()
        players.sort(key=lambda p: p.score, reverse=True)

        return players
