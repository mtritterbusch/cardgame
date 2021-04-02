from unittest import TestCase

from cardgame.classes.cardgame_draw3 import Draw3Game
from cardgame.classes.cardgame import MaxPlayersHit


class TestDraw3(TestCase):

    def test_init_defaults(self):
        draw3 = Draw3Game()

        self.assertEqual(2, draw3.min_players)
        self.assertEqual(8, draw3.max_players)
        self.assertEqual(0, draw3.round_num)
        self.assertEqual(0, draw3.turn_num)
        self.assertEqual(3, draw3.num_rounds)

    def test_setup_game(self):
        draw3 = Draw3Game()
        self.assertRaises(
            MaxPlayersHit,
            draw3.setup_game,
            player_names=[
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
            ]
        )
