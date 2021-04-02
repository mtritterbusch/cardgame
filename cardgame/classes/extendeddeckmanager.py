from .deckmanager import DeckManager, InvalidDeckError


class ExtendedDeckManager(DeckManager):
    """
    ExtendedDeckManager class:  adds some helper methods and
        additional constructors to DeckManager
        allows custom decks

    Constructors:
        ExtendedDeckManager.from_suits_and_values(
            suits_ranking,      # suits list (low to high)
            values_ranking,     # values list (low to high)
        )
        ExtendedDeckManager.from_deck(
            initial_deck,       # list of Card() expected
            suits_ranking=None, # optional ranking of suits (low to high)
            values_ranking=None # optional values ranking (low to high)
        ):
            classmethod where you can supply your own deck, suits ranking and
            values ranking


    Notes:

        Not part of initial requirements, but pretending that through
            client discovery of additional requirements, this class
            was created
    """
    def __init__(self):
        super().__init__()

    @classmethod
    def from_suits_and_values(cls, suits_ranking, values_ranking):
        # instantiate normal class
        ret_class = cls()

        if suits_ranking is None or not isinstance(suits_ranking, list):
            raise InvalidDeckError

        if len(suits_ranking) == 0:
            # if suits ranking is supplied,
            # we need at least 1 item
            raise InvalidDeckError

        # make copy to prevent outside modification
        ret_class._suits_ranking = suits_ranking.copy()

        if values_ranking is None or not isinstance(values_ranking, list):
            # we expect a list
            raise InvalidDeckError

        if len(values_ranking) == 0:
            # if values ranking is supplied,
            # we need at least 1 item
            raise InvalidDeckError

        # make copy to prevent outside modification
        ret_class._values_ranking = values_ranking.copy()

        # make a copy to prevent outside modifications
        ret_class._deck = ExtendedDeckManager.make_deck(
            ret_class._suits_ranking,
            ret_class._values_ranking
        )

        return ret_class

    @classmethod
    def from_deck(cls, initial_deck, suits_ranking=None, values_ranking=None):
        # initial_deck is expected to be in natural order
        # sanity checks on supplied deck
        # we could allow tuple of tuples
        if not isinstance(initial_deck, list):
            # we expect a list
            raise InvalidDeckError

        # do we care if the supplied deck is empty?

        # instantiate normal class
        ret_class = cls()

        if suits_ranking is not None:
            if not isinstance(suits_ranking, list):
                # we expect a list
                raise InvalidDeckError
            elif len(suits_ranking) == 0:
                # if suits ranking is supplied,
                # we need at least 1 item
                raise InvalidDeckError

            # make copy to prevent outside modification
            ret_class._suits_ranking = suits_ranking.copy()

        if values_ranking is not None:
            if not isinstance(values_ranking, list):
                # we expect a list
                raise InvalidDeckError
            elif len(values_ranking) == 0:
                # if values ranking is supplied,
                # we need at least 1 item
                raise InvalidDeckError

            # make copy to prevent outside modification
            ret_class._values_ranking = values_ranking.copy()

        # make a copy to prevent outside modifications
        # reverse copy to put top card at end of list
        ret_class._deck = initial_deck.copy()[::-1]

        return ret_class

    def empty_deck(self):
        self._deck = []

    def peek_card(self, index):
        try:
            # assume index is in natural order and 1-based
            # our internal deck is reversed, so convert
            # natural, 1-based index to reversed 0-based
            return self._deck[len(self._deck) - index]
        except IndexError:
            return None
