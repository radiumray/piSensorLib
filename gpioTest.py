#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


LEDPin=16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin,GPIO.OUT)


while True:
    try:
        GPIO.output(LEDPin,True)
        time.sleep(1)
        GPIO.output(LEDPin,False)
        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        #GPIO.close()
        print("exit")


'''
from gpiozero import LED
from time import sleep

led = LED(17)
print('hhhhhh')

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
'''