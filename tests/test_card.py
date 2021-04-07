"""
test_card.py:  tests for Card() class
"""
from unittest import TestCase

from cardgame.classes.card import Card


class TestCard(TestCase):
    """
    TestCard():  tests for Card() class
    """
    def test_card_creation(self):
        """
        test_card_creation():
            test Card() creation and values
        """
        card = Card('Suit', 'Value', 1, 2)
        self.assertEqual('Suit', card.suit)
        self.assertEqual('Value', card.value)
        self.assertEqual(1, card.suit_value)
        self.assertEqual(2, card.card_value)

    def test_card_comparison(self):
        """
        test_card_comparison():
            test > and == between different cards
        """
        card1 = Card('Suit1', 'Value1', 1, 2)
        card2 = Card('Suit2', 'Value2', 2, 3)
        card3 = Card('Suit1', 'Value1', 1, 2)
        card4 = Card('Suit1', 'Value4', 1, 4)

        self.assertGreater(card2, card1)
        self.assertEqual(card1, card3)
        self.assertLess(card1, card4)

    def test_card_copy(self):
        """
        test_card_copy():  test to make sure copy of card matches
        """
        card1 = Card('Suit1', 'Value1', 1, 2)
        card_copy = card1.__copy__()

        self.assertEqual(card1, card_copy)

    def test_card_str(self):
        """
        test_card_str():  test str and repr of Card()
        """
        suit = "SuitX"
        suit_value = 5
        value = "ValueY"
        card_value = 6

        expected_str = ", ".join(
            [
                f"Card({suit}",
                f"{value}",
                f"{suit_value}",
                f"{card_value})",
            ]
        )

        card = Card(suit, value, suit_value, card_value)
        self.assertEqual(expected_str, str(card))
        self.assertEqual(expected_str, card.__repr__())
