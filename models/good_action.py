from models.action import Action

class GoodAction(Action):
	def __init__(self, name, id_next_scene):
		super().__init__(name)
		self.id_next_scene = id_next_scene

	def get_message(self):
		return ''

	def stop_input(self):
		return False
