import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pwm = 50

btn1 = 5
btn2 = 6

led = 18

GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

p = GPIO.PWM(led, 50)
p.start(pwm)


try:
	while 1:
		if GPIO.input(btn1) == 0:
			pwm = pwm + 5
			if pwm > 100:
				pwm = 100
			p.ChangeDutyCycle(pwm)
			time.sleep(0.1)
			print("button 1 pressed")
		elif GPIO.input(btn2) == 0:
			pwm = pwm - 5
			if pwm < 0:
				pwm = 0
			p.ChangeDutyCycle(pwm)
			time.sleep(0.1)
			print("button 2 pressed")
		else:
			print("No button pressed")
finally:
	print("cleaning up")
	GPIO.cleanup()
