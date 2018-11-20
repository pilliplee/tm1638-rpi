# CP320 - Final Project
# Author: Alex Kirsopp and Pillip Lee
# Version 5

import spidev
import time
channel=0

spi=spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz = 5000

def infrared_On():
	try:
		while True:
			adc=spi.xfer2([1,(8+channel)<<4,0])
			data=((adc[1]&3)<<8) +adc[2]
			data_scale=(data*3.3)/float(1023)
			data_scale=round(data_scale, 2)
			print (data_scale)
			print("\n")
			if data_scale > 0:
				return data_scale

	except KeyboardInterrupt:
		pass

	spi.close()
