from game import Game
from data.scenario import load_scenario

scenario = load_scenario()
game = Game(scenario)
game.run()
