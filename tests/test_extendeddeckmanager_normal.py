"""
test_extendeddeckmanager_normal.py:
    ExtendedDeckManager() defaults to normal deck
    and should pass all DeckManager() tests
"""
from cardgame.classes.extendeddeckmanager import ExtendedDeckManager

from .test_deckmanager_normal import TestDeckManager


# pylint: disable=too-few-public-methods
class TestExtendedDeckManagerNormal(TestDeckManager):
    """
        TestExtendedDeckManagerNormal():
            reuses tests against TestDeckManager() because
            they all should pass
    """
    # ExtendedDeckManager() defaults should pass
    # all DeckManager() tests
    @staticmethod
    def create_deck_manager():
        """
        create_deck_manager():
            override to create ExtendedDeckManager() to be used
            on all tests in test_deckmanager_normal.TestDeckManager()
        """
        return ExtendedDeckManager()
