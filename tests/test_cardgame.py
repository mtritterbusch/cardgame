"""
test_cardgame.py
    tests for base CardGame class
"""
from cardgame.classes.cardgame import (
    CardGame,
    NeedMorePlayers,
    MaxPlayersHit,
    InvalidPlayerName,
    DeckNotInitialized
)
from cardgame.classes.deckmanager import DeckManager

from .test_player_deckmanager import TestPlayerDeckManager


class SampleGame(CardGame):
    """
    SampleGame()
        helper class for testing a class that inherits
        the CardGame class
    """
    def __init__(self):
        super().__init__()
        self._deck_mgr = DeckManager()
        self._min_players = 2
        self._max_players = 3

    def setup_game(self, *args, **kwargs):
        """
        setup_game()
            required to be implemented
        """

    def start_game(self):
        """
        start_game()
            required to be implemented
        """
        if len(self._players) < self._min_players:
            raise NeedMorePlayers


class TestCardGame(TestPlayerDeckManager):
    """
    TestCardGame():
        tests for base CardGame class
    """
    def test_cardgame_nit_class(self):
        """
        test_cardgame_init_class()
            test to make sure initial values are set
            as we expect
        """
        game = CardGame()
        self.assertRaises(DeckNotInitialized, game.deck)
        self.assertEqual(0, game.min_players)
        self.assertEqual(0, game.max_players)
        self.assertEqual(True, game.random_turn_order)

    def test_cardgame_methods(self):
        """
        test_cardgame_methods()
            test expected behavior of methods on CardGame()
        """
        game = CardGame()
        game.random_turn_order = False
        self.assertEqual(False, game.random_turn_order)
        # test methods right after initialization
        self.assertEqual([], game.get_turn_order())
        self.assertEqual([], game.get_current_players())
        self.assertRaises(NotImplementedError, game.setup_game)
        self.assertRaises(NotImplementedError, game.start_game)
        self.assertRaises(MaxPlayersHit, game.add_player, "TestPlayer1")

        # test with minimal inherited CardGame() wrapper
        game = SampleGame()
        self.assertEqual(1, game.add_player("TestPlayer1"))
        self.assertRaises(NeedMorePlayers, game.start_game)
        # InvalidPlayerName check happens before MaxPlayersHit check
        self.assertRaises(InvalidPlayerName, game.add_player, object())
        self.assertNotEqual([], game.deck())
        self.assertEqual(None, game.new_round(1))
        game.remove_all_players()
        self.assertEqual([], game.get_current_players())
        self.assertEqual([], game.get_turn_order())
