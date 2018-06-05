# Homework 2, Problem 1
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time
# LEDs
pins = [17, 18, 27] # LED 1, LED 2, LED 3

# setup all pins for the LEDs and then set the LEDs to off
for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)

try:
	while True:
		# prompt for which LED to turn on
		LED_index = input("what LED?")
		# if the input is between 1 and 3
		# then light up the cooresponding LEDs
		if LED_index <= 3 and LED_index >= 1:
			# lights up the LED that matches the LED_index given
			# and all other LEDs with a lower LED_index
			# i.e. if input is 3 light up LEDs 1 - 3
			for i in range(LED_index):
				GPIO.output(pins[i], 1)
			# turn of all other LEDs	
			for i in range(LED_index, 3):
				GPIO.output(pins[i], 0)
		# if the input is not within the valid range of 1 - 3
		# then state that the LED number was invalid
		else:
			print("Invalid LED number")
except KeyboardInterrupt:		
	GPIO.cleanup()
