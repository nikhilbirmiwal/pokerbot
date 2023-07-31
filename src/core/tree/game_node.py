from __future__ import annotations

import copy

import src.core.common.cards as cards
from src.core.common.constants import Action, GameState, PlayerState, Position
from src.core.tree.node import Node


class PlayerInformation:
    def __init__(self, hand: cards.Hand):
        self.hand = hand

        self.playerState = PlayerState.IN_HAND
        self.potContributionsBb = 0.0
        self.stackSizeBb = 100.0  # TODO: plumb this constant through from the Game

    def __del__(self):
        del self.hand

    def __str__(self):
        if self.playerState == PlayerState.NOT_IN_HAND:
            return "<>"

        return "({}/{}) with {}bbs".format(
            str(self.hand[0]), str(self.hand[1]), self.stackSizeBb
        )


class GameNode(Node):
    def __init__(
        self,
        deck: cards.Deck,
        player_information: dict,
        potSizeBb: float,
        currBetBb: float,
        currPlayer: Position,
        state: GameState,
    ):
        self.deck = deck
        self.player_information = player_information
        self.potSizeBb = potSizeBb
        self.currBetBb = currBetBb
        self.currPlayer = currPlayer
        self.state = state

    def __del__(self):
        del self.player_information

    def __str__(self) -> str:
        res = "Pot {}bb, curr bet = {}bb\n".format(self.potSizeBb, self.currBetBb)
        for _, position in enumerate(Position):
            res += "{}{}: {}\n".format(
                ">" if self.currPlayer == position else " ",
                position,
                str(self.player_information[position]),
            )

        return res

    @staticmethod
    def root() -> GameNode:
        deck = cards.Deck()
        player_information = {}
        for _, position in enumerate(Position):
            player_hole_cards = deck.deal(2)
            player_hole_cards.sort()
            hand = cards.Hand(player_hole_cards)
            player_information[position] = PlayerInformation(hand)
        node = GameNode(
            deck, player_information, 0.0, 0.0, Position.SB, GameState.PREFLOP
        )
        node.__doBet(0.5)
        node.__doBet(1.0)
        return node

    def __doBet(self, bb: float):
        state = self.player_information[self.currPlayer]
        if bb < 0 or state.stackSizeBb - bb < 0:
            raise ValueError(
                "Cannot do bet of {}, has {}".format(bb, state.stackSizeBb)
            )

        state.stackSizeBb -= bb
        state.potContributionsBb += bb
        self.potSizeBb += bb
        self.currBetBb = bb
        self.currPlayer = Position.next(self.currPlayer)

    def __doAction(self, action: Action) -> None:
        if action == Action.FOLD:
            self.player_information[
                self.currPlayer
            ].playerState = PlayerState.NOT_IN_HAND
            self.currPlayer = Position.next(self.currPlayer)
        else:
            betSize = Action.betSize(action, self.currBetBb, self.potSizeBb)
            self.__doBet(betSize)

    def __positions_in_hand(self) -> list[Position]:
        return [
            p
            for p in Position
            if self.player_information[p].playerState == PlayerState.IN_HAND
        ]

    # TODO(urgent): Switch to an iterator method to avoid blowing out memory usages.
    # Or don't - we intend on porting this to the cloud.
    def children(self) -> list[tuple[Action, Node]]:
        positions_in_hand = self.__positions_in_hand()
        if all(
            self.player_information[position].potContributionsBb == self.currBetBb
            for position in positions_in_hand
        ):
            return []  # TODO(nikhil): Return chance nodes if streets remain

        actions = (
            [Action.CHECK, Action.BET_100]
            if self.currBetBb == 0
            else [Action.CALL, Action.FOLD, Action.BET_100]
        )

        children: list[tuple[Action, Node]] = []
        for action in actions:
            nodeCopy = copy.deepcopy(self)
            nodeCopy.__doAction(action)
            children.append((action, nodeCopy))

        return children
