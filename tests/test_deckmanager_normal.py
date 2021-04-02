from unittest import TestCase

from cardgame.classes.card import Card
from cardgame.classes.deckmanager import DeckManager, EmptyDeckError

from .helper import Helper


class TestDeckManager(TestCase, Helper):
    def create_deck_manager(self):
        return DeckManager()

    def test_normal_deck_creation(self):
        deck_mgr = self.create_deck_manager()
        deck = deck_mgr.deck()
        # test to make sure we have a normal deck length
        self.assertEqual(52, len(deck))
        # test to make sure we have 4 known suits
        # in default ranking order (low to high)
        self.assertEqual(4, len(deck_mgr.suits_ranking()))
        self.assertEqual([
            'Spades',
            'Diamonds',
            'Hearts',
            'Clubs',
        ], deck_mgr.suits_ranking())
        # test to make sure we have expected card values
        # in default order of low to high
        self.assertEqual([
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
        ], deck_mgr.values_ranking())

        # make sure sorting the deck keeps original order
        sorted_deck = deck_mgr.sort()
        self.assertEqual(deck, sorted_deck)
        # make sure we didn't lose any cards on the sort
        self.assertEqual(52, len(deck))
        self.assertEqual(52, len(sorted_deck))

    def test_normal_deck_shuffled(self):
        deck_mgr = self.create_deck_manager()
        original_deck = deck_mgr.deck()
        shuffled_deck = deck_mgr.shuffle()
        # make sure deck has been shuffled
        self.assertNotEqual(original_deck, shuffled_deck)
        # make sure deck mgr internal deck has been shuffed
        self.assertEqual(shuffled_deck, deck_mgr.deck())
        # make sure we didn't lose any cards
        self.assertEqual(52, len(original_deck))
        self.assertEqual(52, len(shuffled_deck))

    def test_normal_deck_order(self):
        deck_mgr = self.create_deck_manager()
        card = deck_mgr.draw_card()
        # make sure card we drew is what we expected
        self.assertEqual(Card('Spades', '2', 1, 2), card)
        # check that first and last card are as expected
        self.assertEqual(Card('Spades', '3', 1, 3), deck_mgr.draw_card())
        for count in range(0, 49):
            deck_mgr.draw_card()
        self.assertEqual(Card('Clubs', 'Ace', 4, 14), deck_mgr.draw_card())

    def test_empty_deck_error_thrown(self):
        deck_mgr = self.create_deck_manager()
        for count in range(52):
            deck_mgr.draw_card()
        # check to make sure EmptyDeckError is thrown
        # if we try to draw a card from an empty deck
        self.assertRaises(EmptyDeckError, deck_mgr.draw_card)
