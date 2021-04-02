from unittest import TestCase

from cardgame.classes.deckmanager import DeckManager
from cardgame.classes.player import Player


class TestPlayerDeckManager(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._testname1 = 'Fred'
        self._testname2 = 'Sally'
        self._player1 = Player(self._testname1)
        self._player2 = Player(self._testname2)
        self._deckmgr = DeckManager()

    def test_player_name(self):
        self.assertEqual(self._testname1, self._player1.name)
        self.assertEqual(self._testname2, self._player2.name)

    def test_player_initial_hand(self):
        self.assertEqual([], self._player1.hand)
        self.assertEqual([], self._player2.hand)

    def test_player_drawcard(self):
        # deck() returns deck in natural order
        deck = self._deckmgr.deck()
        self._player1.draw_card(self._deckmgr)
        self.assertEqual(deck[0], self._player1.hand[0])
        self._player2.draw_card(self._deckmgr)
        self.assertEqual(deck[1], self._player2.hand[0])
