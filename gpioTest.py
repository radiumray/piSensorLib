#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDPin=16
buttonPin=13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin,GPIO.OUT)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.01)

    try:
        if (GPIO.input(buttonPin) == 1):
            GPIO.output(LEDPin, False)
        else:
            GPIO.output(LEDPin, True)
    except (KeyboardInterrupt, SystemExit):
        print("exit")