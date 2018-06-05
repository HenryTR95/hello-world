
import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT);
GPIO.setup(13, GPIO.IN);

GPIO.output(TRIG, False)
time.sleep(0.1)

print "Starting Measurement..."

try:
	while 1:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			pass
		start = time.time()

		while GPIO.input(ECHO) == 1:
			pass
		stop = time.time()

		delta_t = stop - start
		# v = 343 m/s is the speed of sound
		# distance = v*delta_t/2
		# 171.5 is 343/2
		# 2 is because the sound wave travels to the object and then
		# back to sensor
		# 100 is to convert to cm from m
		distance = 171.5*delta_t*100
		
		print distance,
		print "cm"
		time.sleep(0.5)
finally:
	print("cleaning up")
	GPIO.cleanup()
		
