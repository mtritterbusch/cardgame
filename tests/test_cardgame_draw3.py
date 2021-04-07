"""
test_cardgame_draw3.py:
    tests defaults and setup of Draw3Game()
"""
from cardgame.classes.card import Card
from cardgame.classes.cardgame_draw3 import Draw3Game
from cardgame.classes.cardgame import MaxPlayersHit, NeedMorePlayers
from cardgame.classes.deckmanager import DeckManager

from .helper import Helper
from .test_deckmanager_normal import TestDeckManager


class TestDraw3(TestDeckManager):
    """
    TestDraw3():
        tests defaults and basic setup of Draw3Game()
    """

    @staticmethod
    def base_game_setup(num_players):
        """
        base_game_setup():  helper function for base setup
        """
        draw3 = Draw3Game()
        sample_players = Helper.generate_player_names(num_players)
        draw3.setup_game(player_names=sample_players)
        return (draw3, sample_players)

    def test_init_defaults(self):
        """
        test_init_defaults():
            test to make sure defaults are what we expect
        """
        draw3 = Draw3Game()

        self.assertEqual(2, draw3.min_players)
        self.assertEqual(8, draw3.max_players)
        self.assertEqual(1, draw3.round_num)
        self.assertEqual(1, draw3.turn_num)
        self.assertEqual(3, draw3.num_rounds)

    def test_setup_game(self):
        """
        test_setup_game():
            test basic setup assertions and errors
        """
        draw3 = Draw3Game()

        # if we explicitly specify no players, then
        # call to setup game should still have no players
        draw3.setup_game(player_names=None)
        self.assertEqual(0, len(draw3.get_current_players()))

        # test to make sure we can get/set random_turn_order
        # should initially default to True
        self.assertEqual(True, draw3.random_turn_order)
        draw3.random_turn_order = False
        self.assertEqual(False, draw3.random_turn_order)

        # test that we can send in deck on setup
        deck_mgr = DeckManager()
        # setup_game will not shuffle deck if it is supplied
        draw3.setup_game(deck_mgr=deck_mgr)
        self.assertEqual(deck_mgr.deck(), draw3.deck())

        # if we add only 1 player and try to start
        # the game, we should get the exception
        # telling us we need to add more players
        draw3.add_player('Skeeter')
        self.assertRaises(
            NeedMorePlayers,
            draw3.start_game
        )

        # if we remove all players, count should equal 0
        draw3.remove_all_players()
        self.assertEqual(0, len(draw3.get_current_players()))

        # if we try to add too many players,
        # we should get MaxPlayersHit exception
        too_many_players = Helper.generate_player_names(9)
        self.assertRaises(
            MaxPlayersHit,
            draw3.setup_game,
            player_names=too_many_players
        )

    def test_start_game(self):
        """
        test_start_game():
            test various aspects of starting the game
        """
        draw3, sample_players = TestDraw3.base_game_setup(5)
        draw3.random_turn_order = False
        draw3.start_game()
        # players turns should be in order added
        self.assertEqual(sample_players, draw3.get_turn_order())
        draw3.random_turn_order = True
        draw3.start_game()
        # players should be shuffled now
        self.assertNotEqual(sample_players, draw3.get_turn_order())

    def test_next_turn(self):
        """
        test_next_turn():
            tests expectations when turns are processed
        """
        draw3, sample_players = TestDraw3.base_game_setup(3)
        # set to False so we can predict some actions
        draw3.random_turn_order = False
        turn_num_before = draw3.turn_num
        player_before = draw3.get_current_player()
        # order should be preserved
        self.assertEqual(sample_players[0], player_before.name)
        draw3.start_game()
        # on new draw3 obj, turn_num should be same before and
        # after call to start_game()
        self.assertEqual(turn_num_before, draw3.turn_num)
        self.assertEqual(player_before, draw3.get_current_player())

        draw3.next_turn()
        self.assertEqual(turn_num_before+1, draw3.turn_num)
        self.assertEqual(
            sample_players[1],
            draw3.get_current_player().name
        )

        # one turn has been taken, take remaining turns
        for _ in range(8):
            draw3.next_turn()

        # now if we call next_turn() it should return None
        self.assertEqual(None, draw3.next_turn())

    def test_calc_points(self):
        """
        test_calc_points(): test point calculations and
            player rankings
        """
        draw3, _ = TestDraw3.base_game_setup(2)
        # set to False so we can predict some actions
        draw3.random_turn_order = False
        draw3.auto_shuffle = False
        draw3.start_game()
        player1 = draw3.next_turn()
        # player should be holding 2 of Spades
        hand = player1.hand
        self.assertEqual(1, len(hand))
        self.assertEqual(Card('Spades', '2', 1, 2), hand[0])
        # we know what the point should be
        self.assertEqual(2, draw3.calc_points(player1.hand))

        # next card should be 3 of Spades
        player2 = draw3.next_turn()
        hand = player2.hand
        self.assertEqual(1, len(hand))
        self.assertEqual(Card('Spades', '3', 1, 3), hand[0])
        # we know what the point should be
        self.assertEqual(3, draw3.calc_points(player2.hand))

        # now test rankings
        players = draw3.player_rankings()
        # should be 2 players
        self.assertEqual(2, len(players))
        # player2 should be ranked higher than player1
        self.assertEqual(players[0], player2)
