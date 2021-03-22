from models.action import Action

class NoAction(Action):
	def __init__(self, id_next_scene):
		super().__init__('')
		self.id_next_scene = id_next_scene

	def get_message(self):
		return "D'Oh! Invalid input... \n"

	def stop_input(self):
		return False
