from __future__ import annotations

from enum import Enum


class Position(Enum):
    DEALER = 0
    SB = 1
    BB = 2
    UTG = 3
    MP = 4
    CO = 5

    def next(self) -> Position:
        return Position.DEALER
