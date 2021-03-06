"""
player.py:  class to represent a player, hand and score
"""


class InvalidName(Exception):
    """
    InvalidName():  exception thown on trying to set
        the player name with an invalid name
    """


class Player:
    """
    Player class is simple wrapper to hold cards (player's hand)

    Constructors:
    Player(name):  where 'name' is a string

    Attributes:
    name:   Initial name given to Player class
    hand:   returns list of Card() objects currently in this player's hand
    score:  (get/set) player score

    Methods:
    draw_card(deck):  Draws a card from supplied deck (DeckManager object)
    """

    def __init__(self, name):
        if not isinstance(name, str):
            raise InvalidName

        self._name = name
        self._hand = []
        self._score = 0

    def __copy__(self):
        # implement copy method to create copy
        player = Player(self.name)
        player.hand = self.hand
        player.score = self.score
        return player

    def __str__(self):
        return f"Player('{self.name}', hand={self.hand}, score={self.score})"

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        """
        name():  returns player name
        """
        return self._name

    @property
    def hand(self):
        """
        hand():  get/set player hand
        """
        return self._hand.copy()

    @hand.setter
    def hand(self, new_hand):
        # having a setter for player hand allows for more complicated
        # games rules, like players swapping hands on some condition
        self._hand = new_hand.copy()

    @property
    def score(self):
        """
        score():  get/set player score
        """
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score

    def draw_card(self, deck_mgr):
        """
        draw_card(deck_mgr):

        Draws a card from the deck manager object and adds
        it to this player's hand

        if deck is empty will raise error
        do not catch here
        """
        self._hand.append(deck_mgr.draw_card())
