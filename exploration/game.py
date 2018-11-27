# import exploration_button
# import explor_game
from time import sleep
from random import randint 

DIO = 17
CLK = 11
STB = 22


def handle_buttons(button_num):
	print("Button Handler -> Button pressed: ", button_num)
	time.sleep(1)

def main():
	print("CP320 - Exploration Project")
	print("Prepared by: Alex Kirsopp & Pillip Lee")
	final_level = 10
	level = 0

	try:
		while level != final_level:
			explor_game.display_score(level)
			completed = False
			print("Welcome to Level: ", level)
			LED_list = []
			BUTTON_list = []

			for x in range(level):
				n = randint(1,8)
				LED_list.append(n)

			explor_game.led_sequence(LED)
			
			while len(BUTTON_list) != (level+1):
				buttons = exploration_button.TM1638_Button(DIO, CLK, STB)
				print("Waiting for input...")
				buttons.wait_for_input(handle_buttons)
				BUTTON_list.append(buttons)
			print(BUTTON_list)


			if LED_list == BUTTON_list: 	# Check if LED and Button sequences match.
				completed = True
				level += 1
			else:
				print("Program Done.")
				break

	except KeyboardInterrupt:
		pass


main()
