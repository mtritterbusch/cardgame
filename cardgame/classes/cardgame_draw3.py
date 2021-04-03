import random

from cardgame.classes.cardgame import (
    CardGame,
    NeedMorePlayers
)
from cardgame.classes.deckmanager import DeckManager


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

        # this game only has 3 rounds
        self._num_rounds = 3
        self._turn_num = 0
        self._round_num = 0

    @property
    def num_rounds(self):
        return self._num_rounds

    @property
    def turn_num(self):
        return self._turn_num

    @property
    def round_num(self):
        return self._round_num

    def setup_game(self, deck=None, player_names=['Fred', 'Sally']):
        """
        setup_game(
            deck=None,   # can supply a deck
            player_names=['Fred', 'Sally']  # list of player names
        )

        Note:  self.add_player(player_name) will raise MaxPlayersHit
            exception if you try to add more than max players
        """
        if deck is None:
            # default to standard 52-card deck
            self._deck = DeckManager()
            self._deck.shuffle()
        else:
            self._deck = deck

        # calling setup_game() will clear players every time
        self.remove_all_players()
        if player_names:
            for player_name in player_names:
                self.add_player(player_name)

    def start_game(self):
        """
        start_game(random_start=True)
            checks to see if we have at least min required players
                raises NeedMorePlayers exception if below min
            random_start=True to shuffle player turn order
        """
        if len(self._players) < self.min_players:
            raise NeedMorePlayers

        if self.random_turn_order:
            random.shuffle(self._turn_order)

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
                self._turn_num - 1
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
        player.draw_card(self._deck)

        return player

    def calc_points(self, hand):
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
