import src.core.common.cards as cards
from src.core.common.constants import Action, Position
from src.core.player.player import Player
from src.core.tree.node import Node


class PlayerState:
    def __init__(self, hand: cards.Hand, player: Player):
        self.hand = hand
        self.player = player
        self.stackSizeBb = 100  # TODO: plumb this constant through from the Game

    def __str__(self):
        return "{} ({}/{}) with {}bbs".format(
            str(self.player), str(self.hand[0]), str(self.hand[1]), self.stackSizeBb
        )

    def onBet(self, bb: float):
        if bb < 0 or self.stackSizeBb - bb < 0:
            raise ValueError("Cannot do bet of {}, has {}".format(bb, self.stackSizeBb))

        self.stackSizeBb -= bb


class GameNode(Node):
    def __init__(self, players: list[Player]):
        if len(players) != len(Position):
            raise ValueError(
                "Cannot map player to position: {}, {}".format(players, Position)
            )

        self.players = players
        self.deck = cards.Deck()
        """ map position to PlayerState """
        self.player_state = {}
        for i, position in enumerate(Position):
            player_hole_cards = self.deck.deal(2)
            player_hole_cards.sort()
            self.player_state[position] = PlayerState(
                cards.Hand(player_hole_cards), players[i]
            )

        self.curr_player = Position.UTG
        self.is_terminal = False
        self.player_state[Position.SB].onBet(0.5)
        self.player_state[Position.BB].onBet(1.0)

    def __str__(self) -> str:
        res = ""
        for _, position in enumerate(Position):
            res += "{}{}: {}\n".format(
                ">" if self.curr_player == position else " ",
                position,
                str(self.player_state[position]),
            )

        return res

    """ Return all possible children nodes from this node. """

    def children(self) -> list[tuple[Action, Node]]:
        if self.is_terminal:
            return []

        # The player can take one of N actions.
        #   - If there is a previous bet, the player may opt to call, fold, or bet.
        #   - If there is no previous bet, the player may opt to check or bet.
        # If the betting round is closed, then there are M chance node children; the runouts.
        # If there
        return []
