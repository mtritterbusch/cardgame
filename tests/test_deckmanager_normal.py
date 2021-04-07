"""
test_deckmanager_normal.py:
    tests a default DeckManager()
"""
from unittest import TestCase

from cardgame.classes.card import Card
from cardgame.classes.deckmanager import DeckManager, EmptyDeckError

from .helper import Helper


class TestDeckManager(TestCase, Helper):
    """
    TestDeckManager():
        tests against standard DeckManager()
    """
    @staticmethod
    def create_deck_manager():  # pylint: disable=W0221
        """
        create_deck_manager():
            override to return different deck manager
        """
        return DeckManager()

    def test_normal_deck_creation(self):
        """
        test_normal_deck_creation():
            test things about a normal deck that we expect
        """
        deck_mgr = TestDeckManager.create_deck_manager()
        deck = deck_mgr.deck()
        # test to make sure we have a normal deck length
        self.assertEqual(52, len(deck))
        # test to make sure we have 4 known suits
        # in default ranking order (low to high)
        self.assertEqual(4, len(deck_mgr.suits_ranking()))
        self.assertEqual(
            Helper.normal_deck_suits(),
            deck_mgr.suits_ranking()
        )
        # test to make sure we have expected card values
        # in default order of low to high
        self.assertEqual(
            Helper.normal_deck_values(),
            deck_mgr.values_ranking()
        )

        # make sure sorting the deck keeps original order
        sorted_deck = deck_mgr.sort()
        self.assertEqual(deck, sorted_deck)
        # make sure we didn't lose any cards on the sort
        self.assertEqual(52, len(deck))
        self.assertEqual(52, len(sorted_deck))

    def test_normal_deck_shuffled(self):
        """
        test_normal_deck_shuffled():
            tests to make sure shuffling is random
        """
        deck_mgr = TestDeckManager.create_deck_manager()
        original_deck = deck_mgr.deck()
        shuffled_deck = deck_mgr.shuffle()
        # make sure deck has been shuffled
        self.assertNotEqual(original_deck, shuffled_deck)
        # make sure deck mgr internal deck has been shuffed
        self.assertEqual(shuffled_deck, deck_mgr.deck())
        # make sure if we shuffle again, it doesn't equal
        # previously shuffled deck or original deck
        # (technically chances are really, really slim that
        # they could equal each other)
        self.assertNotEqual(shuffled_deck, deck_mgr.shuffle())
        self.assertNotEqual(original_deck, deck_mgr.deck())
        # make sure we didn't lose any cards
        self.assertEqual(52, len(original_deck))
        self.assertEqual(52, len(shuffled_deck))

    def test_normal_deck_order(self):
        """
        test_normal_deck_order():
            test to make sure "top" card on deck matches
                what we expect it to be (if not shuffled)
            test 2nd card the same way
            draw the rest of the cards and make sure
                last card is what we expect it to be
        """
        deck_mgr = TestDeckManager.create_deck_manager()
        card = deck_mgr.draw_card()
        # make sure card we drew is what we expected
        self.assertEqual(Card('Spades', '2', 1, 2), card)
        # check that first and last card are as expected
        self.assertEqual(Card('Spades', '3', 1, 3), deck_mgr.draw_card())
        for _ in range(0, 49):
            deck_mgr.draw_card()
        self.assertEqual(Card('Clubs', 'Ace', 4, 14), deck_mgr.draw_card())

    def test_empty_deck_error_thrown(self):
        """
        test_empty_deck_error_thrown():
            normal deck, draw 52 cards, should raise error
                if you try to draw more cards
        """
        deck_mgr = TestDeckManager.create_deck_manager()
        for _ in range(52):
            deck_mgr.draw_card()
        # check to make sure EmptyDeckError is thrown
        # if we try to draw a card from an empty deck
        self.assertRaises(EmptyDeckError, deck_mgr.draw_card)
