from models.action import Action
from models.bad_action import BadAction

def test_inheritance_from_action():
	assert issubclass(BadAction, Action)
