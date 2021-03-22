import pytest
from models.action import Action

@pytest.fixture
def action():
	return Action('jump')

def test_action_with_name_and_index_next_scene_is_none_by_default(action):
	assert action.name == 'jump'
	assert action.id_next_scene is None

def test_stop_input_is_true(action):
	assert action.stop_input() is True
