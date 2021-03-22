class Action:
	def __init__(self, name):
		self.name = name
		self.id_next_scene = None

	def stop_input(self):
		return True
