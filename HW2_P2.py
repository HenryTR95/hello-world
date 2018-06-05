# Homework 2, Problem 2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

# LEDs
pins = [17, 18, 27]			# LED 1, LED 2, LED 3	
# buttons to control LEDs	
buttons = [5, 6, 13, 12]	# Button 1, 2, 3, & 4

# setup all pins for the LEDs and then set the LEDs to off
for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)
	
# setup all the pins for the buttons
# the buttons are pull down since they are hooked up to 3.3VDC	
for i, button in enumerate(buttons):
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		# if button 1 is pressed then set LED 1 on
		# and set LEDs 2 & 3 off
		if GPIO.input(buttons[0]) == 1:
			GPIO.output(pins[0], 1)
			GPIO.output(pins[1], 0)
			GPIO.output(pins[2], 0)	
		# if button 2 is pressed then set LEDs 1 & 2 on
		# and set LED 3 off
		if GPIO.input(buttons[1]) == 1:
			GPIO.output(pins[0], 1)
			GPIO.output(pins[1], 1)
			GPIO.output(pins[2], 0)
		# if button 3 is pressed then set all LEDs on (1 - 3)
		if GPIO.input(buttons[2]) == 1:
			GPIO.output(pins[0], 1)
			GPIO.output(pins[1], 1)
			GPIO.output(pins[2], 1)
		# if button 4 is pressed then set all LEDs off (1 - 3)
		if GPIO.input(buttons[3]) == 1:
			GPIO.output(pins[0], 0)
			GPIO.output(pins[1], 0)
			GPIO.output(pins[2], 0)
		
except KeyboardInterrupt:
	GPIO.cleanup()
