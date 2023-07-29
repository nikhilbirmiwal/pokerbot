""" Constants for a Rock, Paper, Scissors Simulation. """

from enum import Enum


class Action(Enum):
    UNSPECIFIED = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    UNSPECIFIED = 0
    WIN = 1
    TIE = 2
    LOSS = 3


ACTIONS = [Action.ROCK, Action.PAPER, Action.SCISSORS]
PLAYERS = ["ALICE", "BOBBY"]


# If win, then you have no regrets.
# If tie, then you have some regret for the winning move, and no regret for the losing move.
# If loss, you have a lot of regret for the winning move, and some regret for the tying move.
def GetResult(hero: Action, villain: Action) -> Result:
    if hero == villain:
        return Result.TIE

    if (
        (hero == Action.ROCK and villain == Action.SCISSORS)
        or (hero == Action.PAPER and villain == Action.ROCK)
        or (hero == Action.SCISSORS and villain == Action.PAPER)
    ):
        return Result.WIN

    return Result.LOSS


def FindWinningMove(action: Action) -> Action:
    if action == Action.ROCK:
        return Action.PAPER

    if action == Action.PAPER:
        return Action.SCISSORS

    return Action.ROCK
