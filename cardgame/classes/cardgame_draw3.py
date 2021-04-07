"""
cardgame_draw3.py:

base class used to play Draw3Game()
"""
import random

from .cardgame import (
    CardGame,
    NeedMorePlayers
)
from .deckmanager import DeckManager


class Draw3Game(CardGame):
    """
    Draw3Game:  default is min 2 players, max 8 players
        initial hand each player takes turns drawing a card up to 3
        points per card are suit_value * card_value
        winner has highest number of points
    """
    def __init__(self):
        super().__init__()

        self._min_players = 2
        self._max_players = 8
        self._auto_shuffle = True

        # this game only has 3 rounds
        self._num_rounds = 3
        self._turn_num = 0
        self._round_num = 0

    @property
    def num_rounds(self):
        """
        num_rounds:  returns max number of rounds in this game
        """
        return self._num_rounds

    @property
    def turn_num(self):
        """
        turn_num:  return the turn number within a round
        """
        return self._turn_num + 1

    @property
    def round_num(self):
        """
        round_num:  returns current round in the game
        """
        return self._round_num + 1

    @property
    def auto_shuffle(self):
        """
        auto_shuffle:  whether or not to shuffle deck on start game
        """
        return self._auto_shuffle

    @auto_shuffle.setter
    def auto_shuffle(self, auto_shuffle):
        self._auto_shuffle = auto_shuffle

    # pylint:  disable-msg=W0221
    def setup_game(self, deck_mgr=None, player_names=None):
        """
        setup_game(
            deck_mgr=None,   # can supply a DeckManager() compatible
                object
            player_names=None, players can be added here or
                players can be added via add_player()
        )

        Note:  self.add_player(player_name) will raise MaxPlayersHit
            exception if you try to add more than max players
        """
        if deck_mgr is None:
            # default to standard 52-card deck
            deck_mgr = DeckManager()

        self._deck_mgr = deck_mgr

        # calling setup_game() will clear players every time
        self.remove_all_players()
        if player_names is not None:
            for player_name in player_names:
                self.add_player(player_name)

    def start_game(self):
        """
        start_game()
            checks to see if we have at least min required players
                raises NeedMorePlayers exception if below min
            random_start=True to shuffle player turn order
        """
        if len(self._players) < self.min_players:
            raise NeedMorePlayers

        # reset turns and rounds and players
        self._turn_num = 0
        self._round_num = 0
        for player in self._players:
            player.score = 0

        if self.random_turn_order:
            random.shuffle(self._turn_order)

        if self.auto_shuffle:
            self._deck_mgr.shuffle()

    def is_game_over(self):
        """
        is_game_over()
            for Draw3 game, the game is over after 3 rounds (default)
        """
        return self.round_num > self.num_rounds

    def get_current_player(self):
        """
        get_current_player()
            returns current player (based on turns)
        """
        return self._players[
            self._turn_order[
                self._turn_num
            ]
        ]

    def next_turn(self):
        """
        next_turn()
            processes a turn for the current player
            in the case of Draw3, it is just drawing a card
                from the deck

            returns None on game over
        """
        self._turn_num = (self._turn_num + 1) % len(self._players)
        # current player draws a card
        if self._turn_num == 1:
            self._round_num += 1
            if self.is_game_over():
                # just in case someone calls
                # next_turn() after the game is over
                return None
            self.new_round(self.round_num)
        player = self.get_current_player()
        player.draw_card(self._deck_mgr)

        return player

    @staticmethod
    def calc_points(hand):
        """
        calc_points(hand)
            calculates and returns the points for the current
                hand (from a Player object)
        """
        points = 0
        for card in hand:
            points += card.suit_value * card.card_value

        return points

    def player_rankings(self):
        """
        player_rankings()
            returns the list of Player object with the winner
                at [0] followed by other players
                in descending order
        """
        for player in self._players:
            player.score = self.calc_points(player.hand)

        players = self._players.copy()
        players.sort(key=lambda p: p.score, reverse=True)

        return players
