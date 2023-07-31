from __future__ import annotations

from enum import Enum


class Position(Enum):
    DEALER = 0
    SB = 1
    BB = 2
    UTG = 3
    MP = 4
    CO = 5

    def __str__(self):
        return self.name if self != Position.DEALER else "BN"

    def next(self) -> Position:
        return Position((self.value + 1) % len(Position))


class Action(Enum):
    CHECK = "CHECK"
    CALL = "CALL"
    FOLD = "FOLD"
    BET_100 = "B100"
