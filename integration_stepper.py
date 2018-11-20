# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
stepper_pins=[13,16,26,21]

GPIO.setup(stepper_pins,GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])

steps_for_360 = 2100
multiplier = 5.833

total = 0

def stepper_On(num):
	global total
	print(num)
	val = num

	total += int(val)
	iter = (int(val) * multiplier) / 4
	print("iter %d", iter)

	while iter > 0:
		for row in stepper_sequence:
			GPIO.output(stepper_pins,row)
			time.sleep(0.02)
		iter -= 1

	iter_neutral = (int(360 - total) * multiplier) / 4

	while iter_neutral > 0:
		for row in stepper_sequence:
			GPIO.output(stepper_pins,row)
			time.sleep(0.01)
		iter_neutral -= 1

	return None

GPIO.cleanup()
