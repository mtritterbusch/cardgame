from unittest import TestCase

from cardgame.classes.player import Player, InvalidName
from cardgame.classes.card import Card


class TestPlayer(TestCase):

    def generate_hand(self, suffix, number_of_cards):
        hand = []
        for count in range(number_of_cards):
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
        name = 'Skeeter'
        player = Player(name)
        self.assertEqual(name, player.name)

    def test_bad_name(self):
        name = object()
        self.assertRaises(
            InvalidName,
            Player,
            name
        )

    def test_player_copy(self):
        player1 = Player('Fred')
        player2 = player1.__copy__()

        self.assertNotEqual(player1, player2)

    def test_player_score(self):
        player = Player('Sally')
        self.assertEqual(0, player.score)
        player.score = 10
        self.assertEqual(10, player.score)

    def test_player_hand(self):
        hand1 = self.generate_hand("1", 5)
        hand2 = self.generate_hand("2", 5)
        self.assertNotEqual(str(hand1), str(hand2))
        player = Player('Harold')
        player.hand = hand1
        self.assertEqual(str(hand1), str(player.hand))
        player.hand = hand2
        self.assertNotEqual(str(hand1), str(player.hand))
        self.assertEqual(str(hand2), str(player.hand))
