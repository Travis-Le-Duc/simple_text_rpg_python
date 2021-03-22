from models.action import Action
from models.win_action import WinAction

def test_inheritance_from_action():
	assert issubclass(WinAction, Action)
