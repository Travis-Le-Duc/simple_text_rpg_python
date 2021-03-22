import pytest
from models.action import Action
from models.good_action import GoodAction

@pytest.fixture
def action():
	return GoodAction('run', 32)

def test_inheritance_from_action():
	assert issubclass(GoodAction, Action)

def test_init_with_name_and_index_next_scene(action):
	assert action.name == 'run'
	assert action.id_next_scene == 32

def test_stop_input_is_false(action):
	assert action.stop_input() is False
