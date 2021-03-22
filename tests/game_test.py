import pytest
from game import Game
from models.good_action import GoodAction
from data.scenario import load_scenario

@pytest.fixture
def game(scenario):
	return Game(scenario)

@pytest.fixture
def scenario():
	return load_scenario()

def test_init_current_scene(game, scenario):
	assert game.current_scene == scenario[0]

def test_execute_action(game, scenario):
	any_action = GoodAction('jump', 3)
	game._Game__execute_action(any_action)

	assert game.current_scene == scenario[3]
