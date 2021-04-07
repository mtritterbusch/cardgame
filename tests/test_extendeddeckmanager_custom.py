"""
test_extendeddeckmanager_custom.py:
    test a couple of custom decks
"""
from unittest import TestCase

from cardgame.classes.deckmanager import InvalidDeckError
from cardgame.classes.extendeddeckmanager import ExtendedDeckManager

from .helper import Helper


class TestExtendedDeckManagerCustom(TestCase):
    """
    TestExtendedDeckManagerCustom():
        tests 2 different custom decks
    """
    @staticmethod
    def create_deck_manager():
        """
        create_deck_manager()
            not required in these tests
        """

    def base_tests(self, deck_mgr, deck, suits, values):
        """
        base_tests():
            common set of tests custom decks should pass
        """
        # make sure deck length hasn't changed
        self.assertEqual(len(deck), len(deck_mgr.deck()))
        # length of suits and values should not have changed
        self.assertEqual(len(suits), len(deck_mgr.suits_ranking()))
        self.assertEqual(len(values), len(deck_mgr.values_ranking()))
        # make sure top card is what we expect
        self.assertEqual(
            # deck is expected to be in natural order at this point
            deck[0],
            deck_mgr.peek_card(1)
        )
        # make sure bottom card is what we expect
        self.assertEqual(
            # deck is expected to be in natural order at this point
            deck[-1],
            deck_mgr.peek_card(len(deck_mgr.deck()))
        )

        # make sure shuffle works
        shuffled = deck_mgr.shuffle()
        # check lengths
        self.assertEqual(len(deck), len(shuffled))
        # compare decks
        self.assertNotEqual(deck, shuffled)
        # make sure deck manager internal deck is shuffled
        self.assertEqual(shuffled, deck_mgr.deck())

    def test_create_deck_manager(self):
        """
        test_create_deck_manager()
            test that it returns None
        """
        self.assertEqual(
            None,
            TestExtendedDeckManagerCustom.create_deck_manager()
        )

    def test_invalid_initial_deck(self):
        """
        test_invalid_initial_decks():  test to make sure
            InvalidDeckError is raised when trying to create
            ExtendedDeckManager() from invalid deck
        """
        self.assertRaises(
            InvalidDeckError,
            ExtendedDeckManager.from_deck,
            "junk here",
            None,
            True
        )

    def test_inital_deck(self):
        """
        test_initial_deck():
            run base_tests() against deckmanager built from
                custom #1 in Helper
        """
        suits_ranking, values_ranking = Helper.custom_suits_values_1()
        # make_deck() creates reversed deck
        # convert to natural order deck for testing comparisons
        deck = ExtendedDeckManager.make_deck(suits_ranking, values_ranking)
        deck.reverse()
        # make sure created deck has proper number of cards
        self.assertEqual(
            len(suits_ranking)*len(values_ranking),
            len(deck)
        )

        deck_mgr = ExtendedDeckManager.from_deck(
            deck,
            suits_ranking,
            values_ranking
        )

        self.base_tests(deck_mgr, deck, suits_ranking, values_ranking)

    def test_custom_deck2(self):
        """
        test_custom_deck2():
            run base_tests() against deckmanager built from
                custom #2 in Helper
        """
        suits_ranking, values_ranking = Helper.custom_suits_values_2()
        # make_deck() return reversed deck, convert to natural order
        # for testing comparisons
        deck = ExtendedDeckManager.make_deck(suits_ranking, values_ranking)
        deck.reverse()

        deck_mgr = ExtendedDeckManager.from_suits_and_values(
            suits_ranking,
            values_ranking
        )

        self.base_tests(deck_mgr, deck, suits_ranking, values_ranking)
