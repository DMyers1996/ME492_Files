#Dylan Myers
#ME492 Day 7 Assignment


import RPi.GPIO as GPIO
import time

led_pin = 18
on_switch = 20
off_switch = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(on_switch, GPIO.IN)
GPIO.setup(off_switch, GPIO.IN)

pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(100)

try:
	while True:
		if (GPIO.input(on_switch) == 1):
			count = 0
			while (count != 105):
				pwm_led.ChangeDutyCycle(count)
				time.sleep(.2)
				count = count + 5
		if (GPIO.input(off_switch) == 1):
			count = 100
			while (count != -5):
				pwm_led.ChangeDutyCycle(count)
				time.sleep(.2)
				count = count - 5

finally:
	print('Cleaning up')
	GPIO.cleanup()
