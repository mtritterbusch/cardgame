import random

from cardgame.classes.player import Player


class InvalidNumberOfPlayers(Exception):
    pass


class NeedMorePlayers(Exception):
    pass


class MaxPlayersHit(Exception):
    pass


class InvalidPlayerName(Exception):
    pass


class DeckNotInitialized(Exception):
    pass


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
        self._deck = None
        self._min_players = 0
        self._max_players = 0
        self._players = []
        self._turn_order = []

        random.seed()

    @property
    def min_players(self):
        return self._min_players

    @property
    def max_players(self):
        return self._max_players

    def add_player(self, player_name):
        if not isinstance(player_name, str):
            raise InvalidPlayerName

        if len(self._players) >= self._max_players:
            raise MaxPlayersHit

        self._turn_order.append(len(self._players))
        self._players.append(Player(player_name))
        return len(self._players)

    def setup_game(self, *args, **kwargs):
        # do any setup for the game before starting
        # i.e. add players, init other vars
        raise NotImplementedError

    def start_game(self, random_start=True):
        # start the game
        raise NotImplementedError
