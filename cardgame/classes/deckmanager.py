"""
deckmanager.py:  base deck creating and manipulating methods for
    making and playing card games

NOTE:
creates standard 52-card deck with suits ranked
    (low to high):  Spades, Diamonds, Hearts, Clubs
"""
import random

from .card import Card


class EmptyDeckError(Exception):
    """
    EmptyDeckError:  exception thrown for empty deck errors
    """


class InvalidDeckError(Exception):
    """
    InvalidDeckError:  exception thrown for invalid decks
    """


DEFAULT_SUITS_RANKING = [
    'Spades',
    'Diamonds',
    'Hearts',
    'Clubs',
]

DEFAULT_VALUES_RANKING = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'Jack',
    'Queen',
    'King',
    'Ace',
]


class DeckManager:
    """
    Deck Manager class to manage and perform various operations
    on the deck/cards

    Accepts supplied deck on creation;
        defaults to 52-card Spades, Diamonds, Hearts, Clubs

    Constructors:
        DeckManager():  returns normal 52-card deck with suit ranking
        (low to high) as ['Spades', 'Diamonds', 'Hearts', 'Clubs']

    Methods:
        deck():  returns copy of current deck

    Notes:
        deck is internally stored with "top of deck" at the
        end for list efficiency;
        returned copy of deck will be reversed to preserve natural order

    """

    def __init__(self):
        # suit ranking from low to high
        self._suits_ranking = DEFAULT_SUITS_RANKING

        # card values from low to high
        self._values_ranking = DEFAULT_VALUES_RANKING

        # seed random once
        random.seed()

        self._deck = DeckManager.make_deck(
            self._suits_ranking,
            self._values_ranking
        )

    @staticmethod
    def make_deck(suits, values, suits_value_start=1, cards_value_start=2):
        """
        make_deck(suits, values, suits_value_start=1, cards_value_start=2):
            base deck maker that creates a deck from suits and values
            (list of Card() objects)

        NOTES:
        staticmethod so it can be called without having to create an
            instance of DeckManager()
        """
        # suits_value_start=1 and cards_value_start=2 are default
        # for normal 52-card deck
        deck = []
        # reverse suits and values to put top card at end of list
        suit_value = len(suits) - 1 + suits_value_start
        for suit in suits[::-1]:
            card_value = len(values) - 1 + cards_value_start
            for value in values[::-1]:
                deck.append(Card(suit, value, suit_value, card_value))
                card_value -= 1
            suit_value -= 1

        return deck

    def deck(self):
        """
        deck():  returns copy of deck in natural order
        """
        # reverse deck before returning to display in natural order
        return self._deck.copy()[::-1]

    def suits_ranking(self):
        """
        suits_ranking():  returns copy of suits_ranking list
        """
        return self._suits_ranking.copy()

    def values_ranking(self):
        """
        values_ranking():  returns copy of values_ranking list
        """
        return self._values_ranking.copy()

    def shuffle(self):
        """
        shuffle():  shuffles deck and returns copy in natural order
        """
        random.shuffle(self._deck)
        # return in natural order
        return self._deck.copy()[::-1]

    def sort_algo(self, card):
        """
        sort_algo(card):  base sort algorithm

        NOTE:
        override to change sorting
        """
        # make this be the default sorting algorithm, but part of the class
        # so it can be overridden per-object
        return card.suit_value * len(self._values_ranking) + card.card_value

    def sort(self):
        """
        sort():  sorts deck according to algorithm at self.sort_algo

        NOTE:
        override if you want to change sorting algorithm
        """
        # sort biggest at [0] and smallest at [-1]
        # so you can just pop() off cards
        self._deck.sort(key=self.sort_algo)
        return self._deck.copy()

    def draw_card(self):
        """
        draw_card():
            pops card off the "top" of deck (end of list) and returns it
            returns EmptyDeckError exception on empty/invalid deck
        """
        try:
            return self._deck.pop()
        except IndexError as idx_err:
            raise EmptyDeckError from idx_err
