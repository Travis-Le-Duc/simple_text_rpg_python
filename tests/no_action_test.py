import pytest
from models.action import Action
from models.no_action import NoAction

@pytest.fixture
def action():
	return NoAction(2)

def test_inheritance_from_action():
	assert issubclass(NoAction, Action)

def test_init_with_name_and_index_next_scene(action):
	assert action.name == ''
	assert action.id_next_scene == 2

def test_stop_input_is_false(action):
	assert action.stop_input() is False
