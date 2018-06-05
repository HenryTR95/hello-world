# Homework 3: Problem 1
# Henry Rybolt

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [4, 17, 18, 27, 26, 19, 13, 6];
delta_t = 0.05

for i in leds:
	GPIO.setup(i, GPIO.OUT)

try:
	while True:
		for i in range(8):
			GPIO.output(leds[i], True)
			GPIO.output(leds[i-1], False)
			time.sleep(delta_t)
		for i in range(6):
			GPIO.output(leds[6-i], True)
			GPIO.output(leds[7-i], False)
			time.sleep(delta_t)
		GPIO.output(leds[1], False)
finally:
	print("cleaning up")
	GPIO.cleanup()
