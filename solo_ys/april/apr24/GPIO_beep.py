import RPi.GPIO as GPIO

GPIO.setwarnings(False) # ignore warning
GPIO.setmode(GPIO.BCM) # GPIO pin numbering
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # pin 2 initial value as pulled low (off)

while True:
    input_state = GPIO.input(2)
    if input_state == False:
	print('pressed')
	break