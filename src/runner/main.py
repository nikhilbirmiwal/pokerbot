import src.core.game as game
import src.core.player.player as player

PLAYER_COUNT = 6
STARTING_STACK_BB = 100
STREETS_OF_PLAY = 1
ITERATIONS = 1

players = [player.Player("P{}".format(i)) for i in range(1, PLAYER_COUNT + 1)]
configuration = game.GameConfiguration(players, 100, 1)
g = game.Game.fromConfiguration(configuration)

g.train(ITERATIONS)
