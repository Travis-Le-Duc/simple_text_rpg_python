from models.exit_action import ExitAction
from models.no_action import NoAction

class Scene:
	def __init__(self, id, description, actions =()):
		self.id = id
		self.description = description
		self.actions = (ExitAction(),) + actions

	def find_action(self, name):
		return  next((action for action in self.actions if action.name == name), NoAction(self.id))

	def __get_name_actions(self):
		return [action.name for action in self.actions if action.name != "exit"]

	def get_description_with_actions(self):
		text = self.description + " ("
		text += "/".join(self.__get_name_actions())
		text += ")"
		return text
