from time import sleep
import pytm1638

DIO = 17		# GPIO/BCM 17
CLK = 11		# GPIO/BCM 11
STB = 22		# GPIO/BCM 22

display = pytm1638.TM1638(DIO, CLK, STB)

display.enable(1)

def led_sequence(lst):
	for pos in lst:
		display.set_led(pos, 1)
		sleep(0.5)
		display.set_led(pos, 0)
	return None

def button_sequence():

def display_score(lvl):
	num_byte = [63, 6, 91, 79, 102, 109, 125, 7, 127, 103]		# Values for: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

	display.send_char(0, 63)   # Display Segment 1
	display.send_char(1, 84)   # Display Segment 2

	# Display Segment 5
	display.send_char(4, 56)
	# Display Segment 6
	display.send_char(5, 128)
	# Display Segment 8
	display.send_char(6, num_byte[lvl])

	return None