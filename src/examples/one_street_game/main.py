""" Entrypoint for the one_street_game trainer. """

import src.examples.one_street_game.constants as constants
import src.examples.one_street_game.game as game
import src.examples.one_street_game.player as player

actions = [
    constants.Action.CHECK,
    constants.Action.FOLD,
    constants.Action.BET_100,
]

alice = player.Player("Alice", [constants.Action.CHECK, constants.Action.BET_100])
bob = player.Player(
    "Bob", [constants.Action.CHECK, constants.Action.FOLD, constants.Action.CALL]
)
g = game.Game(actions, [alice, bob])
g.train(100)

print(g)
