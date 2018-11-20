# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import time
import pytm1638

def display_svn_segment(num):
	DIO = 17		# GPIO/BCM 17
	CLK = 21		# GPIO/BCM 11
	STB = 22		# GPIO/BCM 22

	display = pytm1638.TM1638(DIO, CLK, STB)

	display.enable(1)
    num_byte = [ 63, 6, 91, 79, 102, 109, 125, 7, 127, 103] # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

	num = str(("{:.2f}".format(num)))
    seg1 = int(num[0])
    seg2 = num[1]
    seg3 = int(num[2])
    seg4 = int(num[3])

    display.send_char(0, 63)   # 1
    display.send_char(1, 84)  # 2
    
    # Display Segment 5
    display.send_char(4, num_byte[seg1])
    display.set_led(4, 1)
    # Display Segment 6
    display.send_char(5, 128)
    display.set_led(5, 1)
    # Display Segment 7
    display.send_char(6, num_byte[seg3])
    display.set_led(6, 1)
    # Display Segment 8
    display.send_char(7, num_byte[seg4])
    display.set_led(7, 1)

	return None