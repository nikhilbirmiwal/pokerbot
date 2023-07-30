""" A single player in a one street game of poker. """

import random

import src.examples.one_street_game.constants as constants
import src.examples.one_street_game.core as core


class PlayerMemory:
    # Map (node/hand/action) -> regret
    def __init__(self, actions):
        self.actions = actions
        self.memory = {}

    @staticmethod
    def make_key(node: core.Node, hand: core.Hand, action: constants.Action) -> str:
        return "{}.{}.{}".format(str(node), str(hand), str(action))

    def get_regrets(
        self, node: core.Node, hand: core.Hand, actions: list[constants.Action]
    ) -> dict:
        regret_dict: dict = {}
        for action in actions:
            key = PlayerMemory.make_key(node, hand, action)
            if self.memory.get(key) is None:
                self.memory[key] = 1
            regret_dict[action] = self.memory[key]
        return regret_dict


class Player:
    def __init__(self, name: str, actions: list[constants.Action]):
        self.name = name
        self.actions = actions
        self.memory = PlayerMemory(actions)

    def __str__(self):
        return "{}".format(self.name)

    def supported_actions(self, node: core.Node) -> list[constants.Action]:
        if node.betSize == 0:
            return list(
                filter(
                    lambda action: constants.Action.isBet(action)
                    or action == constants.Action.CHECK,
                    self.actions,
                )
            )

        return list(
            filter(
                lambda action: action == constants.Action.FOLD
                or action == constants.Action.CALL
                or constants.Action.isBet(action),
                self.actions,
            )
        )

    def choose_action(self, node: core.Node, hand: core.Hand) -> constants.Action:
        possible_actions = self.supported_actions(node)
        regret_dict = self.memory.get_regrets(node, hand, possible_actions)

        actions = list(regret_dict.keys())
        regrets = list(regret_dict.values())

        # trunk-ignore(bandit/B311)
        choice = random.randint(1, sum(regrets))
        weights = [sum(regrets[: i + 1]) for i in range(0, len(actions))]
        for action in range(0, len(actions)):
            if choice <= weights[action]:
                return actions[action]

        raise Exception(
            "Encountered unreachable code; {} {} {}".format(choice, actions, weights)
        )
