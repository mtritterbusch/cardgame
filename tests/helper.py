"""
helper.py:  helper functions for custom decks
"""


class Helper:  # pragma: no cover
    """
    Helper():  helper functions for custom decks
    """
    @staticmethod
    def custom_suits_values_1():
        """
        custom_suits_values_1():
            sample custom desk to be used in tests
        """
        # returns (suits_ranking, values_ranking)
        return (
            [
                'Diamonds',
                'Hearts',
            ],
            [
                '10',
                'Jack',
                'Queen',
                'King',
            ]
        )

    @staticmethod
    def custom_suits_values_2():
        """
        custom_suits_values_2():
            sample custom deck to be used in tests
        """
        # returns (suits_ranking, values_ranking)
        return (
            [
                'Sith',
                'Jedi',
            ],
            [
                'Youngling',
                'Padawan',
                'Knight',
                'Guardian',
                'Master',
            ]
        )

    @staticmethod
    def create_deck_manager(*args, **kwargs):
        """
        create_deck_manager():  must be implemented by classes
            that inherit this class
        """
        raise NotImplementedError

    @staticmethod
    def normal_deck_suits():
        """
        normal_deck_suits():  returns list of normal deck suits
        """
        return [
            'Spades',
            'Diamonds',
            'Hearts',
            'Clubs',
        ]

    @staticmethod
    def normal_deck_values():
        """
        normal_deck_values():
            returns list of normal deck values
        """
        return [
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
        ]

    @staticmethod
    def generate_player_names(count):
        """
        generate_player_names(): generates list of player names
        """
        return [
            f"Player{x}" for x in range(1, count+1)
        ]
