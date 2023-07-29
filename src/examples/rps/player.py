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

    def update_regrets(self, player_actions):
        player_move = player_actions[self.name]
        opponent_moves = list(
            {k: v for k, v in player_actions.items() if k != self.name}.values()
        )
        if len(opponent_moves) != 1:
            raise Exception("Missing / too many opponent moves")

        opponent_move = opponent_moves[0]
        result = constants.GetResult(player_move, opponent_move)
        preferred_move = constants.FindWinningMove(opponent_move)
        if result == constants.Result.WIN:
            return

        self.regret[preferred_move] += 1

    def strategy(self):
        total_regret = sum(list(self.regret.values()))
        normalized_regret = {}
        for kv in self.regret.items():
            normalized_regret[kv[0]] = format(kv[1] / total_regret, ".0%")
        return normalized_regret
