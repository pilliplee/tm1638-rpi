# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import time
import pytm1638
import RPi.GPIO as GPIO

READ_BTNS = 0x42

class TM1638_Button:
    def __init__(self, dio, clk, stb):
        self.stb = stb
        self.display = pytm1638.TM1638(dio, clk, stb)
        self.display.enable(1)

    def get_exp_val(self, val):
        count = 0
        while val >= 1:
        	val /= 2
        	count += 1;
        return count

    def wait_for_input(self, cb):
        while True:
            res = 0
            GPIO.output(self.stb, False) # Toggle read
            self.display.send_byte(READ_BTNS)

            for i in range(4):
                res |= self.display.receive() << i

            GPIO.output(self.stb, True) # Toggle read

            if res > 0:
                value = self.get_exp_val(res)
                break

            time.sleep(0.1)

        cb(value)
        return res
