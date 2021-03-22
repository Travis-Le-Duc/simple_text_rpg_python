from models.action import Action

class WinAction(Action):
	def __init__(self, name):
		super().__init__(name)

	def get_message(self):
		return "Congratulations! \n"
