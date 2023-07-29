""" A Simulation of a Game. """

import src.examples.rps.constants as constants
import src.examples.rps.player as player


class Game:
    def __init__(self):
        self.players = [
            player.Player(name, constants.ACTIONS) for name in constants.PLAYERS
        ]
        self.iteration = 0

    def __str__(self):
        return "{}: {}".format(self.iteration, [str(player) for player in self.players])

    def play_turn(self):
        player_names = [player.name for player in self.players]
        player_actions = [player.choose_action() for player in self.players]
        action_profile = {
            k: v for (k, v) in zip(player_names, player_actions, strict=True)
        }
        [player.update_regrets(action_profile) for player in self.players]

    def train(self, iterations):
        assert iterations >= 1
        while self.iteration < iterations:
            self.play_turn()
            self.iteration += 1
        print("Finished training!")
