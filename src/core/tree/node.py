from __future__ import annotations

from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def children(self) -> list[Node]:
        pass
