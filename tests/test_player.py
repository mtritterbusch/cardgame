"""
test_player.py:  tests for Player() class
"""
from unittest import TestCase

from cardgame.classes.player import Player, InvalidName
from cardgame.classes.card import Card


class TestPlayer(TestCase):
    """
    TestPlayer():
        tests Player() values and methods
    """
    @staticmethod
    def generate_hand(suffix, number_of_cards):
        """
        generate_hand(suffix, number_of_cards):
            helper function to create a hand(list) of Cards()
        """
        hand = []
        for _ in range(number_of_cards):
            hand.append(
                Card(
                    f"Suit{suffix}",
                    f"Value{suffix}",
                    0,
                    0
                )
            )

        return hand

    def test_name(self):
        """
        test_name:  test setting name for player
        """
        name = 'Skeeter'
        player = Player(name)
        self.assertEqual(name, player.name)

    def test_bad_name(self):
        """
        test_bad_name():  test setting bad name for player
        """
        name = object()
        self.assertRaises(
            InvalidName,
            Player,
            name
        )

    def test_player_copy(self):
        """
        test_player_copy():
            test Player.__copy__() returns new copy
                of Player() not pointer to original
        """
        player1 = Player('Fred')
        player2 = player1.__copy__()

        self.assertNotEqual(player1, player2)

    def test_player_score(self):
        """
        test_player_score():
            test get/set scores
        """
        player = Player('Sally')
        self.assertEqual(0, player.score)
        player.score = 10
        self.assertEqual(10, player.score)

    def test_player_hand(self):
        """
        test_player_hand():
            test setting and comparing custom hands for players
        """
        hand1 = TestPlayer.generate_hand("1", 5)
        hand2 = TestPlayer.generate_hand("2", 5)
        self.assertNotEqual(str(hand1), str(hand2))
        player = Player('Harold')
        player.hand = hand1
        self.assertEqual(str(hand1), str(player.hand))
        player.hand = hand2
        self.assertNotEqual(str(hand1), str(player.hand))
        self.assertEqual(str(hand2), str(player.hand))
