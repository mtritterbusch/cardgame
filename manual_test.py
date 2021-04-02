from cardgame.classes.deckmanager import DeckManager


if __name__ == "__main__":
    test = DeckManager()
    print("\nInitial deck:")
    print(test.deck())
    print("\nShuffled deck:")
    shuffled = test.shuffle()
    print(shuffled)
    print("\nInternal deck:")
    print(test.deck())
    print("\nSorted deck:")
    print(test.sort())
