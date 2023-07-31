from __future__ import annotations

from src.core.player.player import Player
from src.core.tree.game_node import GameNode


class GameConfiguration:
    def __init__(
        self, players: list[Player], startingStackBb: int, streetsOfPlay: int = 3
    ):
        if len(players) != 6:
            raise ValueError("Unsupported player count: {}".format(len(players)))

        if startingStackBb != 100:
            raise ValueError("Unsupported starting stacks: {}".format(startingStackBb))

        if streetsOfPlay != 1 and streetsOfPlay != 3:
            raise ValueError("Unsupported streets of play: {}".format(streetsOfPlay))

        self.players = players
        self.startingStackBb = startingStackBb
        self.streetsOfPlay = streetsOfPlay


class Game:
    def __init__(self, config: GameConfiguration):
        self.config = config
        self.iteration = 0

    @staticmethod
    def fromConfiguration(config: GameConfiguration) -> Game:
        return Game(config)

    def __training_iteration(self) -> None:
        node = GameNode.root()
        for c in node.children():
            print(str(c[0]), str(c[1]))

    def train(self, iterations: int) -> None:
        while self.iteration < iterations:
            self.__training_iteration()
            self.iteration += 1

        print("Finished training {} iterations!".format(iterations))
