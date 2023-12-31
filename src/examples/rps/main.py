""" Entrypoint for RPS app. """

import src.examples.rps.game as game

g = game.Game()
g.train(5000)

for player in g.players:
    print(player.name, player.strategy())
