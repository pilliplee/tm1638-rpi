import exploration_button
import explor_game
import time

DIO = 17
CLK = 11
STB = 22

def handle_buttons(button_num):
	print("Button Handler -> Button pressed: ", button_num)
	time.sleep(1)


def main():
	print("CP320 - Exploration Project")
	print("Prepared by: Alex Kirsopp & Pillip Lee")


	try:
		while True:
            explor_game.display_score()
            # buttons = exploration_button.TM1638_Button(DIO, CLK, STB)
            # print("Waiting for input...")
            # buttons.wait_for_input(handle_buttons)

	except KeyboardInterrupt:
		pass

main()
