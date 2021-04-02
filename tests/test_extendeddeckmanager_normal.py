from cardgame.classes.extendeddeckmanager import ExtendedDeckManager

from .test_deckmanager_normal import TestDeckManager


class TestExtendedDeckManagerNormal(TestDeckManager):
    # ExtendedDeckManager() defaults should pass
    # all DeckManager() tests
    def create_deck_manager(self):
        return ExtendedDeckManager()
