import src.core.common.cards as cards
from src.core.common.constants import Action, Position
from src.core.player.player import Player
from src.core.tree.node import Node


class PlayerState:
    def __init__(self, hand: cards.Hand, stackSizeBb: int):
        self.hand = hand
        self.stackSizeBb = stackSizeBb

    def __str__(self):
        return "({}/{})".format(str(self.hand[0]), str(self.hand[1]))


class GameNode(Node):
    def __init__(self, players: list[Player]):
        """players[i] = p indicates that i is the position (e.g. UTG) of player p."""
        self.players = players
        self.deck = cards.Deck()
        self.player_state = {}
        for player in players:
            player_hole_cards = self.deck.deal(2)
            player_hole_cards.sort()
            hand = cards.Hand(player_hole_cards)
            self.player_state[player] = PlayerState(hand, 100)

        self.curr_player = Position.UTG
        self.is_terminal = False

    def __str__(self) -> str:
        res = ""
        for player in self.players:
            res += "{}: {}\n".format(str(player), str(self.player_state[player]))

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
