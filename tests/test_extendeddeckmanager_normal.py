"""
test_extendeddeckmanager_normal.py:
    ExtendedDeckManager() defaults to normal deck
    and should pass all DeckManager() tests
"""
from cardgame.classes.card import Card
from cardgame.classes.deckmanager import InvalidDeckError
from cardgame.classes.extendeddeckmanager import ExtendedDeckManager

from .helper import Helper
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

    def test_create_deck_manager(self):
        """
        test_create_deck_manager()
            tests to make sure create_deck_manager()
            returns ExtendedDeckManager()
        """
        self.assertEqual(
            True,
            isinstance(
                TestExtendedDeckManagerNormal.create_deck_manager(),
                ExtendedDeckManager
            )
        )

    def test_from_suits_and_values(self):
        """
        test_from_suits_and_values()
            test classmethod
            from_suits_and_values(suits_ranking, values_ranking)
        """
        suits = Helper.normal_deck_suits()

        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_suits_and_values,
            None,
            None
        )
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_suits_and_values,
            [],
            None
        )
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_suits_and_values,
            suits,
            None
        )
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_suits_and_values,
            suits,
            []
        )

    def test_from_deck(self):
        """
        test_from_deck()
            test classmethod
            from_deck(
                initial_deck,
                suits_ranking=None,
                values_ranking=None
            )
        """
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_deck,
            None
        )
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_deck,
            "A,K,Q,J,10"
        )

        # now build a valid deck
        deck = ExtendedDeckManager.make_deck(
            Helper.normal_deck_suits(),
            Helper.normal_deck_values()
        )

        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_deck,
            deck,
            "1,2,3,4",
            None
        )
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_deck,
            deck,
            None,
            "1,2,3,4,5,6,7"
        )
        deck_mgr = ExtendedDeckManager.from_deck(
            deck
        )
        # should be 52 card deck right now
        self.assertEqual(52, len(deck_mgr.deck()))
        # top card
        self.assertEqual(
            Card("Spades", "2", 1, 2),
            deck_mgr.peek_card(52)
        )
        deck_mgr.empty_deck()
        # now should be 0
        self.assertEqual(0, len(deck_mgr.deck()))
        # no card
        self.assertEqual(
            None,
            deck_mgr.peek_card(1)
        )
