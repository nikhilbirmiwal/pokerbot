""" A one street Poker game. """

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


class Game:
    def __init__(self, players):
        if len(players) < 2:
            raise Exception("Invalid argument; must specify at least `2` players")

        self.players = players
        self.deck = Deck()
        self.iteration = 0

    def __str__(self):
        return "Iteration {}: {}".format(self.iteration, [str(p) for p in self.players])

    def do_turn(self):
        hole_cards = {}
        hand_history = []
        for p in self.players:
            hole_cards[p.name] = self.deck.draw(2)

        for p in self.players:
            p_cards = hole_cards[p.name]
            # TODO: Implement a state machine on valid actions.
            p_action = p.choose_action(hand_history, p_cards)
            hand_history.append(str(p_action))

        # TODO: Compute Payoff Utilities
        # TODO: Can we support negative payoff utilities? How do we translate payoff utilities into regrets?
        print("Iteration", self.iteration)
        for p in self.players:
            print(p.name, [str(card) for card in hole_cards[p.name]])
        print(hand_history)
        print()

    def train(self, iterations):
        if iterations <= 0:
            raise Exception(
                "Invalid training iteration specified: {}".format(iterations)
            )

        while self.iteration < iterations:
            self.do_turn()
            self.deck.reset()
            self.iteration += 1

        print("Finished training {}".format(iterations))
