from typing import TypedDict

import pydealer

from src.core.player.player import Player
from src.core.tree.node import Node


class HoleCards(TypedDict):
    player: Player
    cards: list[pydealer.card.Card]


class GameNode(Node):
    def __init__(self):
        self.name = ""

    def children(self) -> list[Node]:
        return []
