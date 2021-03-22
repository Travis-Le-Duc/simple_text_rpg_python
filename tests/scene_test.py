import pytest
from models.scene import Scene
from models.good_action import GoodAction
from models.exit_action import ExitAction
from models.no_action import NoAction

@pytest.fixture
def action3(scene2):
	return GoodAction('forward', scene2)

@pytest.fixture
def scene2():
	return Scene(2, 'bla bla...')

@pytest.fixture
def scene1(action3, scene2):
	action1 = GoodAction('left', scene2)
	action2 = GoodAction('right', scene2)
	scene = Scene(1, 'my description', (action1, action2, action3))
	return scene

def test_scene_with_description_and_actions_including_one_exit_action_by_default(scene1):
	assert scene1.description== "my description"
	assert len(scene1.actions) == 4
	assert isinstance(scene1.actions[0], ExitAction)

def test_find_actions_returning_the_action_of_forward(scene1, action3):
	assert scene1.find_action('forward') == action3

def test_find_actions_returning_a_no_action_if_not_found(scene1):
	assert isinstance(scene1.find_action('jump'), NoAction)

def test_get_name_actions(scene1):
	assert scene1._Scene__get_name_actions() == ['left', 'right', 'forward']

def test_get_description_with_actions(scene1):
	assert scene1.get_description_with_actions() == "my description (left/right/forward)"
