import pytest
from models.exit_action import ExitAction
from models.action import Action

@pytest.fixture
def exit_action():
	return ExitAction()

def test_inheritance_from_action():
	assert issubclass(ExitAction, Action)

def test_action_with_exit_as_name_by_default(exit_action):
	assert exit_action.name == 'exit'
