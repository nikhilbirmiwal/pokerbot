""" A single player in a one street game of poker. """

import random


class Regrets:
    def __init__(self, actions):
        self.regrets = {
            k: v for (k, v) in zip(actions, [1] * len(actions), strict=True)
        }

    def choose_action(self):
        actions = list(self.regrets.keys())
        regrets = list(self.regrets.values())

        total_regret = sum(regrets)
        # trunk-ignore(bandit/B311)
        choice = random.randint(1, total_regret)
        weights = [sum(regrets[: i + 1]) for i in range(0, len(actions))]
        for action in range(0, len(actions)):
            if choice <= weights[action]:
                return actions[action]

        raise Exception("Encountered unreachable code")


## TODO: cleaner separation of public and private information, e.g. hand history (public) vs. hole cards (private)
## Memory: (game node) -> (regrets)
## A game node consists of:
##   - A list of previous actions.
##   - Current hole cards.
class PlayerMemory:
    def __init__(self, actions):
        self.actions = actions
        self.memory = {}

    def node_key(history, hand):
        # TODO: dedupe (A, B) and (B, A)
        history_str = str([str(x) for x in history])
        hand_str = str([str(x) for x in hand])
        return "{}.{}".format(history_str, hand_str)

    def get_regrets(self, history, hand):
        key = PlayerMemory.node_key(history, hand)
        if self.memory.get(key) is None:
            self.memory[key] = Regrets(self.actions)
        return self.memory[key]


class Player:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
        self.memory = PlayerMemory(actions)

    def __str__(self):
        return "{}".format(self.name)

    def choose_action(self, history, hand):
        regrets = self.memory.get_regrets(history, hand)
        return regrets.choose_action()
