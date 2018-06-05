from numpy import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

def buttonPushed():
	GPIO.output(17, True)
	GPIO.output(27, False)
	time.sleep(0.2)
	print('button pushed')

def buttonNotPushed():
	GPIO.output(17, False)
	GPIO.output(27, True)
	time.sleep(0.05)
	print('button not pushed')
		
while True:
	input_state = GPIO.input(13)
	if input_state == False:
		buttonPushed()
	else:
		buttonNotPushed()
