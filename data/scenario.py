from models.scene import Scene
from models.good_action import GoodAction
from models.win_action import WinAction
from models.bad_action import BadAction
from models.exit_action import ExitAction

def load_scenario():
	scene0 = Scene(
			0,
			"You are Homer Simpson, you want to drink a beer in bar... \n Are you ready?",
			(
				GoodAction("yes", 1),
				ExitAction("no")
			)
	)

	scene1 = Scene(
			1,
			"You are in the living room, where do you go?",
			(
				GoodAction("entrance", 2),
				GoodAction("kitchen", 3)
			)
	)

	scene2 = Scene(
			2,
			"You are opening the entrance door to leave but you meet Marge, she is angry and order you to stay at home to keep an eye on children... \n It's over for the beer today. \n Want to try again?",
			(
				GoodAction("yes", 0),
				BadAction("no")
			)
	)

	scene3 = Scene(
			3,
			"You are now in the kitchen, you want go out through the window but you see the oven that catches fire. You have two choices; \n a: The most important is my beer, go out through the window \n b: Stop the fire \n What do you do?",
			(
				GoodAction("a", 5),
				GoodAction("b", 4)
			)
	)

	scene4 = Scene(
			4,
			"You are trying to put out fire, but you burn yourself. \n You are now in the hospital for several days... \n Want to try again?",
			(
				GoodAction("yes", 0),
				BadAction("no")
			)
	)

	scene5 = Scene(
			5,
			"You're finally out, you walk to the bar. Then you go into the bar, you are so happy! You ask the barman Moe for a beer. But your children and Marge are showing up! Your are learning the house is burned and Marge is very angry. \n You have two choices: Apologize to Marge and go to home or ignore the family and drink your beer.",
			(
				GoodAction("apologize", 6),
				WinAction("drink")
			)
	)

	scene6 = Scene(
			6,
			"You're going to home and it's over for the beer...  \n Want to try again?",
			(
				GoodAction("yes", 0),
				BadAction("no")
			)
	)

	scenario = scene0, scene1, scene2, scene3, scene4, scene5, scene6
	return scenario
