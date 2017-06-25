#Dylan Myers
#ME492_HW2_P2

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pins = [4,17,18,27]

for pin in led_pins:
	GPIO.setup(pin, GPIO.OUT)

for pin in led_pins:
	GPIO.output(pin,1)
	time.sleep(.5)
	GPIO.output(pin,0)

led_pinsR = list(reversed(led_pins))
led_pinsR.remove(led_pinsR[0])
for pin in led_pinsR:
	GPIO.output(pin,1)
	time.sleep(.5)
	GPIO.output(pin,0)

GPIO.cleanup()
