import random

import src.examples.one_street_game.constants as constants


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{}{}".format(str(self.rank), str(self.suit))


class Deck:
    def __init__(self):
        self.reset()

    def reset(self):
        self.cards = [
            Card(rank, suit) for rank in constants.Rank for suit in constants.Suit
        ]

    def draw(self, count):
        if count < 0 or count > len(self.cards):
            raise Exception(
                "Cannot draw {} out of {} cards".format(count, len(self.cards))
            )

        selected = []
        for _ in range(0, count):
            # trunk-ignore(bandit/B311)
            choice = random.randrange(0, len(self.cards))
            selected.append(self.cards[choice])
            del self.cards[choice]

        return selected


class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def __str__(self):
        return str([str(card) for card in self.cards])


# All public information about a game node.
class Node:
    def __init__(self, potSize=100):
        self.history = []
        self.potSize = potSize
        self.betSize = 0

    def __str__(self):
        return "Pot Size: {}. Actions: {}".format(self.potSize, self.history)

    def update(self, action: constants.Action) -> None:
        self.history.append(action)
        if constants.Action.isBet(action):
            self.betSize = constants.Action.betSize(action, self.potSize)
            self.potSize += self.betSize
