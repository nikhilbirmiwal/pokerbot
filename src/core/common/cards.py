from pydealer import deck, stack


class Hand:
    def __init__(self, hand: stack.Stack):
        self.hand = hand

    def __getitem__(self, item):
        return self.hand[item]


class Deck:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.deck = deck.Deck()
        self.deck.shuffle()

    def deal(self, num: int):
        return self.deck.deal(num)
