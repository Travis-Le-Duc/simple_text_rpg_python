from models.action import Action

class ExitAction(Action):
	def __init__(self, name ='exit'):
		super().__init__(name)

	def get_message(self):
		return "See you soon... \n"
