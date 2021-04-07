"""
card.py

uses total_ordering and implements __eq__() and __lt__()
    so that one Card() class can be compared against another
"""
from functools import total_ordering


@total_ordering
class Card:
    """
    Card class:  simple class to access cards by properties

    Notes:
    suit_rank:  int value of suit ranking (higher numbers rank higher),
        setting suit_rank equal to a different suit allows for
        different suits with same value to be equal in comparison
    """
    def __init__(self, suit, value, suit_value, card_value):
        self._suit = suit
        self._value = value
        self._suit_value = suit_value
        self._card_value = card_value

    def __copy__(self):
        # implement copy method to create copy
        return Card(self.suit, self.value, self.suit_value, self.card_value)

    def __str__(self):
        # implement for debugging or printing
        return ", ".join(
            [
                f"Card({self.suit}",
                f"{self.value}",
                f"{self.suit_value}",
                f"{self.card_value})",
            ]
        )

    def __repr__(self):
        return str(self)

    def __eq__(self, cmp):
        return (
            self.suit_value == cmp.suit_value
        ) and (
            self.card_value == cmp.card_value
        )

    def __lt__(self, cmp):
        if self.suit_value == cmp.suit_value:
            return self.card_value < cmp.card_value

        return self.suit_value < cmp.suit_value

    @property
    def suit(self):
        """
        suit:  returns string value of suit
        """
        return self._suit

    @property
    def value(self):
        """
        value:  returns string value of card
        """
        return self._value

    @property
    def suit_value(self):
        """
        suit_value:  returns numeric value of suit
        """
        return self._suit_value

    @property
    def card_value(self):
        """
        card_value:  return numeric value of card
        """
        return self._card_value
