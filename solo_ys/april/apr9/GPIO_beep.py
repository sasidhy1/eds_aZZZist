import RPi.GPIO as GPIO
import pi_beep

GPIO.setwarnings(False) # ignore warning
GPIO.setmode(GPIO.BOARD) # physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pin 10 initial value as pulled low (off)

while True:
    if GPIO.input(10) == GPIO.HIGH:
	    pi_beep