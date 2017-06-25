# test
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# pin = 18
# GPIO.setup(pin, GPIO.OUT)
# p = GPIO.PWM(pin, 50)
# p.start(7.5)
# try:
        # while True:
		# p.ChangeDutyCycle(2.5)
		# time.sleep(1) # sleep 1 second
		# p.ChangeDutyCycle(7.5)
		# time.sleep(1) # sleep 1 second
		# p.ChangeDutyCycle(12.5)
                # time.sleep(1) # sleep 1 second 
# except KeyboardInterrupt:
	# p.stop()
        # GPIO.cleanup()


# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

while True:
        for pulse in range(50, 250, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
        for pulse in range(250, 50, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)