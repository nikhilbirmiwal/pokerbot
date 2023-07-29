""" Constants for a Rock, Paper, Scissors Simulation. """

from enum import Enum


class Action(Enum):
    UNSPECIFIED = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


ACTIONS = [Action.ROCK, Action.PAPER, Action.SCISSORS]
PLAYERS = ["ALICE", "BOBBY"]
