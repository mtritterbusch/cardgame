"""
test_cardgame_draw3.py:
    tests defaults and setup of Draw3Game()
"""
from unittest import TestCase

from cardgame.classes.cardgame_draw3 import Draw3Game
from cardgame.classes.cardgame import MaxPlayersHit, NeedMorePlayers


class TestDraw3(TestCase):
    """
    TestDraw3():
        tests defaults and basic setup of Draw3Game()
    """

    def test_init_defaults(self):
        """
        test_init_defaults():
            test to make sure defaults are what we expect
        """
        draw3 = Draw3Game()

        self.assertEqual(2, draw3.min_players)
        self.assertEqual(8, draw3.max_players)
        self.assertEqual(0, draw3.round_num)
        self.assertEqual(0, draw3.turn_num)
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
        self.assertRaises(
            MaxPlayersHit,
            draw3.setup_game,
            player_names=[
                'p1',
                'p2',
                'p3',
                'p4',
                'p5',
                'p6',
                'p7',
                'p8',
                'p9',
            ]
        )
