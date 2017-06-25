#Dylan Myers
#ME492 Summer 2017
#HW1 Problem 4

#LED Pinout test
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time
pin1 = 17
pin2 = 18
pin3 = 27
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)


entry = input('Enter a number ')

if entry == 1:
	GPIO.output(pin1,1)
elif entry == 2:
	GPIO.output(pin1,1)
	GPIO.output(pin2,1)
elif entry == 3:
	GPIO.output(pin1,1)
	GPIO.output(pin2,1)
	GPIO.output(pin3,1)
else:
	print 'Invalid entry'
time.sleep(1)
GPIO.output(pin1,0)
GPIO.output(pin2,0)
GPIO.output(pin3,0)

GPIO.cleanup()
