"""
test_player_deckmanager.py:
    tests Player() interactions with DeckManager()
"""
from cardgame.classes.deckmanager import DeckManager
from cardgame.classes.player import Player

from .test_player import TestPlayer
from .test_deckmanager_normal import TestDeckManager


class TestPlayerDeckManager(TestPlayer, TestDeckManager):
    """
    TestPlayerDeckManager():
        tests Player() interactions with DeckManager()
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._testname1 = 'Fred'
        self._testname2 = 'Sally'
        self._player1 = Player(self._testname1)
        self._player2 = Player(self._testname2)
        self._deckmgr = DeckManager()

    def test_player_name(self):
        """
        test_player_name():
            tests that players' names match what was assigned to them
        """
        self.assertEqual(self._testname1, self._player1.name)
        self.assertEqual(self._testname2, self._player2.name)

    def test_player_initial_hand(self):
        """
        test_player_initial_hand():
            tests that initial players' hands are empty lists
        """
        self.assertEqual([], self._player1.hand)
        self.assertEqual([], self._player2.hand)

    def test_player_drawcard(self):
        """
        test_player_drawcard():
            tests for making sure drawing a card matches what is
                in players' hands and place in deck
        """
        # deck() returns deck copy in natural order
        deck = self._deckmgr.deck()
        self._player1.draw_card(self._deckmgr)
        self.assertEqual(deck[0], self._player1.hand[0])
        self._player2.draw_card(self._deckmgr)
        self.assertEqual(deck[1], self._player2.hand[0])
