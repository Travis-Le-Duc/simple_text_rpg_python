from models.action import Action

class BadAction(Action):
	def __init__(self, name):
		super().__init__(name)

	def get_message(self):
		return "Game over \n"
