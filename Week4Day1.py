import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_num = 18
GPIO.setup(pin_num, GPIO.OUT)

try:
	while True:
		GPIO.output(pin_num, True)
		time.sleep(0.05)
		GPIO.output(pin_num, False)
		time.sleep(0.099)
finally:
	print("cleaning up")
	GPIO.cleanup()
