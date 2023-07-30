""" A one street Poker game. """


import src.examples.one_street_game.core as core


class Game:
    def __init__(self, players):
        if len(players) < 2:
            raise Exception("Invalid argument; must specify at least `2` players")

        self.players = players
        self.deck = core.Deck()
        self.iteration = 0

    def __str__(self):
        return "Iteration {}: {}".format(self.iteration, [str(p) for p in self.players])

    def do_turn(self) -> None:
        hole_cards = {}
        for p in self.players:
            hole_cards[p.name] = self.deck.draw(2)

        node = core.Node()

        for p in self.players:
            p_cards = hole_cards[p.name]
            p_action = p.choose_action(node, p_cards)
            node.update(p_action)

        # TODO: Compute Payoff Utilities
        # TODO: Can we support negative payoff utilities? How do we translate payoff utilities into regrets?
        print("Iteration", self.iteration)
        for p in self.players:
            print(p.name, [str(card) for card in hole_cards[p.name]])
        print(node)
        print()

    def train(self, iterations: int) -> None:
        if iterations <= 0:
            raise Exception(
                "Invalid training iteration specified: {}".format(iterations)
            )

        while self.iteration < iterations:
            self.do_turn()
            self.deck.reset()
            self.iteration += 1

        print("Finished training {}".format(iterations))
