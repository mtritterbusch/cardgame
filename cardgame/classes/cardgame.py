"""
cardgame.py:  base class for card games
"""
import random

from .player import Player


class NeedMorePlayers(Exception):
    """
    NeedMorePlayers:  exception thrown when trying to
        start a game with too few players
    """


class MaxPlayersHit(Exception):
    """
    MaxPlayersHit:  exception thrown when trying to add
        more than max players
    """


class InvalidPlayerName(Exception):
    """
    InvalidPlayerName:  exception thrown when trying to create
        player with invalid name
    """


class DeckNotInitialized(Exception):
    """
    DeckNotInitialized:  exception thrown when starting a game
        before building the deck
    """


class CardGame:
    """
    CardGame class:  base class that contains the framework to
        implement the logic/rules for playing and
        winning card games

    card games derived from this class need to implement:
        * rules about number of players (min/max)
        * rules about setting up initial hands
        * rules about turn order
        * rules about winning a round/hand/game
    """
    def __init__(self):
        self._deck_mgr = None
        self._min_players = 0
        self._max_players = 0
        self._players = []
        self._turn_order = []
        self._random_turn_order = True

        random.seed()

    def deck(self):
        """
        deck:  returns copy of deck in natural order
        """
        if self._deck_mgr is None:
            raise DeckNotInitialized

        # returns in natural order
        return self._deck_mgr.deck()

    @property
    def min_players(self):
        """
        min_players():  returns min players allow for this game
        """
        return self._min_players

    @property
    def max_players(self):
        """
        max_players():  returns max players allow for this game
        """
        return self._max_players

    @property
    def random_turn_order(self):
        """
        random_turn_order():  get/set if turn order is shuffled or
            by order of player added
        """
        return self._random_turn_order

    @random_turn_order.setter
    def random_turn_order(self, value):
        self._random_turn_order = value

    def get_turn_order(self):
        """
        get_turn_order():  returns names of players in turn order
        """
        return [
            self._players[idx].name for idx in self._turn_order
        ]

    def remove_all_players(self):
        """
        remove_all_players():  removes all players
        """
        self._players = []
        self._turn_order = []

    def get_current_players(self):
        """
        get_current_players(): returns copy of current players
        """
        return self._players.copy()

    def add_player(self, player_name):
        """
        add_player(player_name):
            expects string player_name
            checks that adding player will not exceed max players
            adds Player(player_name) to end of player list
        """
        if not isinstance(player_name, str):
            raise InvalidPlayerName

        if len(self._players) >= self._max_players:
            raise MaxPlayersHit

        self._turn_order.append(len(self._players))
        self._players.append(Player(player_name))
        return len(self._players)

    def setup_game(self, *args, **kwargs):
        """
        setup_game(*args, **kwargs):
            called to perform any setup/initialization of the game

        NOTE:
        method must be implemented
        """
        # do any setup for the game before starting
        # i.e. add players, init other vars
        raise NotImplementedError

    def start_game(self):
        """
        start_game(random_start=True):
            starts game, random_start=True implies random turn order
            for players, if random_start=False, turn order is in
            the order players were added

        NOTE:
        method must be implemented
        """
        # start the game
        raise NotImplementedError

    def new_round(self, round_num):
        """
        new_round(round_num):  called when new round starts

        NOTE:
        override to perform action at this notification
        """
        # called when a new round starts
