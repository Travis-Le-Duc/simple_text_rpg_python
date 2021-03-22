class Game:
	def __init__(self, scenario):
		self.scenario = scenario
		self.current_scene = scenario[0]

	def run(self):
		self.__print_description()
		self.__get_input()

	def __print_description(self):
		print(self.current_scene.get_description_with_actions())

	def __execute_action(self, action):
		print(action.get_message())
		self.current_scene = self.scenario[action.id_next_scene] if action.id_next_scene is not None else None
		
	def __get_input(self):
		while True:
			input_user = input()
			action = self.current_scene.find_action(input_user)

			self.__execute_action(action)
			if action.stop_input() : break

			self.__print_description()
