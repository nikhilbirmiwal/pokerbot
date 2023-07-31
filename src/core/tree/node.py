from __future__ import annotations

from abc import ABC, abstractmethod

from src.core.common.constants import Action


class Node(ABC):
    @abstractmethod
    def children(self) -> list[tuple[Action, Node]]:
        pass
