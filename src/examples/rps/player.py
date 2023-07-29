""" A single player in the RPS game. """

import random

import src.examples.rps.constants as constants


class Player:
    def __init__(self, name: str, actions: list[constants.Action]):
        self.name = name
        self.actions = actions

        regrets = [1] * len(actions)
        self.regret = {k: v for (k, v) in zip(self.actions, regrets, strict=True)}

    def __str__(self):
        return "{} ({})".format(self.name, self.regret)

    def choose_action(self):
        actions = list(self.regret.keys())
        regrets = list(self.regret.values())

        # trunk-ignore(bandit/B311)
        choice = random.randrange(0, sum(regrets))
        weights = [sum(regrets[: i + 1]) for i in range(0, len(actions))]
        for action in range(0, len(actions)):
            if choice <= weights[action]:
                return actions[action]

        raise Exception("Encountered unreachable code")

    def preferred_move(action):
        if action == constants.Action.ROCK:
            return constants.Action.PAPER

        if action == constants.Action.PAPER:
            return constants.Action.SCISSORS

        return constants.Action.ROCK

    def update_regrets(self, player_actions):
        opponent_moves = list(
            {k: v for k, v in player_actions.items() if k != self.name}.values()
        )
        if len(opponent_moves) != 1:
            raise Exception("Missing / too many opponent moves")

        self.regret[Player.preferred_move(opponent_moves[0])] += 1

    def strategy(self):
        total_regret = sum(list(self.regret.values()))
        normalized_regret = {}
        for kv in self.regret.items():
            normalized_regret[kv[0]] = f"{100 * kv[1]/total_regret:2.2f}%"
        return normalized_regret
