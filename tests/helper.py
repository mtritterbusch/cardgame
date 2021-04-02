class Helper:
    def custom_suits_values_1(self):
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

    def custom_suits_values_2(self):
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

    def create_deck_manager(self, *args, **kwargs):
        raise NotImplementedError
